export const channel = new WebSocket("ws://127.0.0.1:8000/ws/lesson/");

channel.onmessage = (event) => {
    console.log(event.data);
};

channel.onerror = (e) => {
    console.log(e);
};
