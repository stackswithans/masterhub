import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Call


class CallConsumer(WebsocketConsumer):
    def connect(self):
        # Add user data here
        self.accept()

    def disconnect(self):
        # Remove user from group if he was connectrd
        if getattr(self, "group_name", None):
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name, self.channel_name
            )
        self.accept()

    def receive(self, text_data):
        msg = json.loads(text_data)
        ms_type = msg["type"]
        if ms_type == "join-call":
            # Add channel to call group
            self.group_name = msg["callId"]
            async_to_sync(self.channel_layer.group_add)(
                self.group_name, self.channel_name
            )
            call = Call.objects.get(callId=self.call_id)
            # Make the first client to connect the polite peer
            call.participants += 1
            call.participants.save()
            response = {"type": "join-accept", "polite": "true"}
            if call.participants == 2:
                response["polite"] = "false"
        self.send(text_data=json.dumps(response))
