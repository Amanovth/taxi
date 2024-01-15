from geopy.distance import distance
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Driver, Tariff
from .serializers import NearestDriversListSerializer, CheckSerializer


class NearestDriversListAPIView(ListAPIView):
    serializer_class = NearestDriversListSerializer
    queryset = Driver.objects.all()


def index(request):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})


class CheckAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Tariff.objects.all()
    serializer_class = CheckSerializer

    def get(self, request, *args, **kwargs):
        from_ = self.request.data.get("from")
        to_ = self.request.data.get("to")

        return self.list(request, *args, **kwargs)
