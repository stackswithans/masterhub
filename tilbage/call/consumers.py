import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Call


class CallConsumer(WebsocketConsumer):
    def connect(self):
        # Add user data here
        self.group_name = None
        self.call = None
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

    def call_peer_type(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "type": "peer-type",
                    "polite": event["polite"],
                }
            )
        )
