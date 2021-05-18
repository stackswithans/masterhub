import { host } from "./utils";

type onTrackCallback = (
    track: MediaStreamTrack,
    streams: MediaStream[]
) => void;

export const joinCall = (callId: String, fn: onTrackCallback) => {
    const hostname = new URL(host).host;
    const channel = new WebSocket(`ws://${hostname}/ws/call`);

    //Send connect message as soon as channel opens
    channel.onopen = () => {
        channel.send(
            JSON.stringify({
                type: "join_call",
                callId: callId,
            })
        );
    };

    //Channel message handler
    channel.onmessage = (event) => {
        console.log(event.data);
    };

    channel.onerror = (e) => {
        console.log(e);
    };
};
