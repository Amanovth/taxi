from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Rental
from src.drivers.models import Driver
from .serializers import (
    CallSerializer,
    CallListSerializer,
    AcceptCallSerializer,
    HistorySerializers,
    HistoryDetailSerializers,
)
from .services import address_decoding
from datetime import datetime

class CallView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CallSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address_a = address_decoding(
            serializer.validated_data["lon_a"], serializer.validated_data["lat_a"]
        )
        address_b = ""
        if serializer.validated_data["lon_b"] and serializer.validated_data["lat_b"]:
            address_b += address_decoding(
                serializer.validated_data["lon_b"], serializer.validated_data["lat_b"]
            )

        # driver = Driver.objects.order_by('?').first()

        passenger_lat = float(serializer.validated_data["lat_a"])
        passenger_lon = float(serializer.validated_data["lon_a"])

        driver_pos = float("inf")
        closest_driver = None

        for driver in Driver.objects.filter(status=2):
            driver_position = abs(passenger_lat - float(driver.lat)) + abs(
                passenger_lon - float(driver.lon)
            )

            if driver_position < driver_pos:
                driver_pos = driver_position
                closest_driver = driver

        if closest_driver:
            serializer.save(
                passenger=request.user,
                driver=closest_driver,
                point_a_street=address_a,
                point_b_street=address_b,
            )
            return Response(
                {
                    "response": True,
                    "message": "Ваш заказ был принят!",
                    "name": f"{closest_driver.user.first_name}",
                    "car_brand": f"{closest_driver.car_brand} {closest_driver.car_model}",
                    "car_color": f"{closest_driver.car_color}",
                    "number_auto": f"{closest_driver.number_auto}",
                },
                status=status.HTTP_201_CREATED,
            )


class CallListView(generics.ListAPIView):
    queryset = Rental.objects.filter(status="request").order_by("-id")
    serializer_class = CallListSerializer


class AcceptCallView(generics.CreateAPIView):
    serializer_class = AcceptCallSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user.user_type == "driver":
            try:
                call = Rental.objects.get(pk=serializer.data["call_id"])

                # Водитель принимает заказ
                if call.status == "request":
                    call.driver = request.user.driver
                    call.status = "driver-accepted"
                    call.save()
                    return Response({"response": True, "message": "Заказ принят таксистом!"}, status=status.HTTP_201_CREATED,)
                # Водитель вас ждёт
                if call.status == "driver-accepted":
                    call.driver = request.user.driver
                    call.status = "driver-waiting"
                    call.save()
                    return Response({"response": True, "message": "Вы прибыли в пункт назначения"}, status=status.HTTP_201_CREATED,)
                # В Пути
                if call.status == "driver-waiting":
                    call.driver = request.user.driver
                    call.status = "on-the-way"
                    call.time_start = datetime.now()
                    call.save()
                    return Response({"response": True, "message": "Пристегните ремни безопасности!"}, status=status.HTTP_201_CREATED,)
                # Поездка завершено
                if call.status == "on-the-way":
                    call.driver = request.user.driver
                    call.status = "completed"
                    call.save()
                    return Response({"response": True, "message": "Поездка завершено!"}, status=status.HTTP_201_CREATED,)
                # Обьект не существует
                return Response({"response": False, "message": "Заказ был завершен!"})
            
            except Rental.DoesNotExist:
                return Response(
                    {"response": False, "message": "Обьект не существует!"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(
            {"response": False, "message": "Вы не являетесь таксистом!"},
            status=status.HTTP_403_FORBIDDEN,
        )


class HistoryAPIView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = HistorySerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Rental.objects.filter(passenger=user, status__in=['completed', 'cancelled'])
    


class HistoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Rental.objects.all()
    serializer_class = HistoryDetailSerializers