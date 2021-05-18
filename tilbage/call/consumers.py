import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Call


class CallConsumer(WebsocketConsumer):
    def connect(self):
        # Add user data here
        self.group_name = None
        self.accept()

    def disconnect(self):
        # Remove user from group if he was connectrd
        if self.group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name, self.channel_name
            )

    def receive(self, text_data):
        msg = json.loads(text_data)
        ms_type = msg["type"]
        if ms_type == "join_call":
            # Add channel to call group
            self.group_name = msg["callId"]
            async_to_sync(self.channel_layer.group_add)(
                self.group_name, self.channel_name
            )
            # Send new_participant message to group
            async_to_sync(self.channel_layer.group_send)(
                self.group_name, {"type": "new_participant", "message": "ni"}
            )
            call = Call.objects.get(callId=self.group_name)
            # Consider the first client to connect as the polite peer
            call.participants += 1
            call.save()
            response = {"type": "join-accept", "polite": "true"}
            if call.participants == 2:
                response["polite"] = "false"
        self.send(text_data=json.dumps(response))
