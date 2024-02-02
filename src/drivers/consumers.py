import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from .models import Driver


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))



class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        if user.is_authenticated:
            await self.channel_layer.group_add(
                f"user_{user.id}",
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        user = self.scope['user']
        if user.is_authenticated:
            await self.channel_layer.group_discard(
                f"user_{user.id}",
                self.channel_name
            )

    async def receive(self, text_data):
        user = self.scope['user']
        data = json.loads(text_data)
        lat = data['lat']
        lon = data['lon']

        driver = await self.get_driver(user)
        driver.lat = lat
        driver.lon = lon
        driver.save()

        await self.send_location_update(user, lat, lon)

    @staticmethod
    async def get_driver(user):
        return await async_to_sync(Driver.objects.get)(user=user)

    async def send_location_update(self, user, lat, lon):
        await self.channel_layer.group_send(
            f"user_{user.id}",
            {
                'type': 'location_update',
                'lat': lat,
                'lon': lon
            }
        )

    async def location_update(self, event):
        lat = event['lat']
        lon = event['lon']

        await self.send(text_data=json.dumps({
            'lat': lat,
            'lon': lon
        }))