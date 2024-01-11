from geopy.distance import distance
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Driver
from .serializers import NearestDriversListSerializer


class NearestDriversListAPIView(APIView):
    def post(self, request, *args, **kwargs):
        passenger_latitude = request.data.get('lat')
        passenger_longitude = request.data.get('lon')

        drivers = Driver.objects.all()

        distances = [
            (driver, distance((driver.lat, driver.lon), (passenger_latitude, passenger_longitude)).km)
            for driver in drivers
        ]

        nearest_positions = sorted(distances, key=lambda x: x[1])[:5]

        serializer = NearestDriversListSerializer(
            [driver for driver, _ in nearest_positions],
            many=True,
            context={'request': request}
        )

        return Response(serializer.data)


from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})
