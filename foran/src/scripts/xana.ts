import { host } from "./utils";

type onTrackCallback = (
    track: MediaStreamTrack,
    streams: MediaStream[]
) => void;

export const joinCall = (callId: String, fn: onTrackCallback) => {
    const hostname = new URL(host).host;
    const channel = new WebSocket(`ws://${hostname}/ws/call`);

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
                console.log("i was accepted");
                break;
            case "peer-type":
                console.log("my peer type is polite: " + message.polite);
                break;
        }
    };

    channel.onerror = (e) => {
        console.log(e);
    };
};
