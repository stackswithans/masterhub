import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Call


class CallConsumer(WebsocketConsumer):
    def connect(self):
        self.call_id = self.scope["url_route"]["kwargs"]["call_id"]
        self.group_name = self.call_id
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        self.accept()

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        ms_type = text_data_json["type"]
        if ms_type == "connect":
            call = Call.objects.get(callId=self.call_id)
            # Make the first client to connect the polite peer
            call.participants += 1
            call.participants.save()
            response = {"message": "connect", "polite": "true"}
            if call.participants == 2:
                response["polite"] = "false"
        self.send(text_data=json.dumps(response))
