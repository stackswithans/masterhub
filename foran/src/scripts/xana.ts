import { host } from "./utils";

type onTrackCallback = (
    track: MediaStreamTrack,
    streams: readonly MediaStream[]
) => void;

class CallConnection {
    callId: String;
    pc: RTCPeerConnection;
    polite: boolean;
    makingOffer: boolean = false;
    ignoreOffer: boolean = false;
    channel: WebSocket;

    constructor(callId: string, channel: WebSocket) {
        this.callId = callId;
        this.pc = new RTCPeerConnection({
            iceServers: [
                {
                    urls: [
                        "stun:stun.l.google.com:19302",
                        "stun:stun1.l.google.com:19302",
                        "stun:stun2.l.google.com:19302",
                        "stun:stun3.l.google.com:19302",
                        "stun:stun4.l.google.com:19302",
                    ],
                },
            ],
        });
        this.channel = channel;
        this.polite = false;
        //Signal channel setup
        channel.onopen = () => {
            channel.send(
                JSON.stringify({
                    type: "join-call",
                    callId: callId,
                })
            );
            this.configurePerfectNegotiation();
        };
    }

    async sendLocalDescription() {
        await this.pc.setLocalDescription();
        this.channel.send(
            JSON.stringify({
                type: "offer-answer",
                description: this.pc.localDescription,
            })
        );
    }

    configurePerfectNegotiation() {
        this.pc.onnegotiationneeded = async () => {
            try {
                this.makingOffer = true;
                await this.sendLocalDescription();
            } catch (err) {
                console.error(err);
            } finally {
                this.makingOffer = false;
            }
        };
        // Handle ice candidate
        this.pc.onicecandidate = ({ candidate }) =>
            this.channel.send(
                JSON.stringify({ type: "ice-candidate", candidate })
            );
        // Handle incoming offers or answers
        this.channel.onmessage = async (event) => {
            const message = JSON.parse(event.data);
            try {
                switch (message.type) {
                    case "join-accept":
                        console.log("Connection to call succesfull");
                        break;
                    case "peer-type":
                        this.polite = message.polite == "true";
                        console.log(
                            "my peer type is polite: " + message.polite
                        );
                        break;
                    case "offer-answer":
                        const offerCollision =
                            message.description.type == "offer" &&
                            (this.makingOffer ||
                                this.pc.signalingState != "stable");

                        this.ignoreOffer = !this.polite && offerCollision;
                        if (this.ignoreOffer) {
                            return;
                        }
                        await this.pc.setRemoteDescription(message.description);
                        if (message.description.type == "offer") {
                            await this.sendLocalDescription();
                        }
                        break;
                    case "ice-candidate":
                        this.pc
                            .addIceCandidate(message.candidate)
                            .then()
                            .catch((err) => console.log(err));
                        break;
                }
            } catch (err) {
                console.log(err);
            }
        };
    }
}

export const joinCall = (
    callId: string,
    localStream: MediaStream,
    fn: onTrackCallback
) => {
    const hostname = new URL(host).host;
    const channel = new WebSocket(`ws://${hostname}/ws/call`);
    const conn = new CallConnection(callId, channel);

    channel.onerror = (e) => {
        console.log(e);
    };
    // Transmit to remote peer
    localStream
        .getTracks()
        .forEach((track) => conn.pc.addTrack(track, localStream));

    //Call remote peer stream handler
    conn.pc.ontrack = ({ track, streams }) => fn(track, streams);
};
