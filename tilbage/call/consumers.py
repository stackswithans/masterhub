import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Call


class CallConsumer(WebsocketConsumer):
    def connect(self):
        # Add user data here
        self.group_name = None
        self.call = None
        self.peer = None
        self.accept()

    def disconnect(self, close_code):
        # Remove user from group if he was connectrd
        if self.group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name, self.channel_name
            )

    def receive(self, text_data):
        msg = json.loads(text_data)
        ms_type = msg["type"]
        if ms_type == "join-call":
            # Add channel to call group
            self.group_name = msg["callId"]
            # Send new_participant message to group
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "call_new_participant",
                    "new_channel": self.channel_name,
                },
            )
            # Add channel to group
            async_to_sync(self.channel_layer.group_add)(
                self.group_name, self.channel_name
            )
            response = {"type": "join-accept", "message": ""}
        elif ms_type in ("offer-answer", "ice-candidate"):
            # Ice candidate are sent before other peer connects
            if self.peer is None:
                return
            # Forward offer/answer to other peer
            data = {
                "type": "call_peer_send",
                "ms_type": ms_type,
            }
            if ms_type == "offer-answer":
                data["description"] = msg["description"]
            else:
                data["candidate"] = msg["candidate"]
            async_to_sync(self.channel_layer.send)(self.peer, data)
            return
        self.send(text_data=json.dumps(response))

    def call_new_participant(self, event):
        # If consumer gets new participant event, it means that he was first
        # to join channel, therefore he should be the polite peer
        async_to_sync(self.channel_layer.send)(
            self.channel_name, {"type": "call_peer_type", "polite": "true"}
        )
        async_to_sync(self.channel_layer.send)(
            event["new_channel"], {"type": "call_peer_type", "polite": "false"}
        )
        # Connect to the other end of the channel
        self.peer = event["new_channel"]
        async_to_sync(self.channel_layer.send)(
            event["new_channel"],
            {"type": "call_connect", "peer": self.channel_name},
        )

    def call_peer_send(self, event):
        data = {**event}
        del data["type"]
        self.send(text_data=json.dumps({"type": event["ms_type"], **data}))

    def call_peer_type(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "type": "peer-type",
                    "polite": event["polite"],
                }
            )
        )

    def call_connect(self, event):
        if self.peer is not None:
            return
        self.peer = event["peer"]
