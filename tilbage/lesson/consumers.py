import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class LessonConsumer(WebsocketConsumer):
    def connect(self):
        # self.lesson_id = self.scope["url_route"]["kwargs"]["lesson_id"]
        # Join room group
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        print(message)
        self.send(
            text_data=json.dumps({"message": f"Server echoes: {message}"})
        )
