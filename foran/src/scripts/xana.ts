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
    }

    configureNegotiation() {
        this.pc.onnegotiationneeded = async () => {
            try {
                this.makingOffer = true;
                await this.pc.setLocalDescription();
                this.channel.send(
                    JSON.stringify({ description: this.pc.localDescription })
                );
            } catch (err) {
                console.error(err);
            } finally {
                this.makingOffer = false;
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
    // Transmit to remote peer
    localStream
        .getTracks()
        .forEach((track) => conn.pc.addTrack(track, localStream));

    //Call remote peer stream handler
    conn.pc.ontrack = ({ track, streams }) => fn(track, streams);

    //Signal channel setup
    channel.onopen = () => {
        channel.send(
            JSON.stringify({
                type: "join-call",
                callId: callId,
            })
        );
    };

    channel.onmessage = (event) => {
        console.log(event.data);
        const message = JSON.parse(event.data);
        switch (message.type) {
            case "join-accept":
                console.log("Connection to call succesfull");
                break;
            case "peer-type":
                conn.polite = message.polite == "true";
                console.log("my peer type is polite: " + message.polite);
                break;
        }
    };

    channel.onerror = (e) => {
        console.log(e);
    };
};
