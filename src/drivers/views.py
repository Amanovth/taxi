from geopy.distance import distance
from rest_framework import generics
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Driver, Tariff
from .serializers import NearestDriversListSerializer, CheckSerializer, RatingSerializers


class NearestDriversListAPIView(ListAPIView):
    serializer_class = NearestDriversListSerializer
    queryset = Driver.objects.all()


def index(request):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})


class CheckAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tariff.objects.all()
    serializer_class = CheckSerializer

    def get(self, request, *args, **kwargs):
        from_ = self.request.data.get("from")
        to_ = self.request.data.get("to")

        return self.list(request, *args, **kwargs)



class RatingAPIView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = RatingSerializers
    
    def post(self, request, *args, **kwargs):
        serializer = RatingSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        driver = Driver.objects.get(pk=serializer.validated_data['driver_id'])
        driver.total_star = int(driver.total_star) + serializer.validated_data['rating']
        driver.users_star = int(driver.users_star) + 1
        driver.star = driver.total_star / driver.users_star
        driver.save()
        return Response({'message': 'Cпасибо за ваш отзыв!'}, status=status.HTTP_201_CREATED)
    