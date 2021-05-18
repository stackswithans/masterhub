import { host } from "./utils";

type onTrackCallback = (
    track: MediaStreamTrack,
    streams: MediaStream[]
) => void;

export const joinCall = (callId: String, fn: onTrackCallback) => {
    const hostname = new URL(host).host;
    const channel = new WebSocket(`ws://${hostname}/ws/call`);
    channel.onmessage = (event) => {
        console.log(event.data);
    };

    channel.onerror = (e) => {
        console.log(e);
    };
};
