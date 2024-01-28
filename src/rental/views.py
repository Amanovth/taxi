from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Rental
from .serializers import CallSerializer, CallListSerializer, AcceptCallSerializer


class CallView(generics.CreateAPIView):
    serializer_class = CallSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(passenger=request.user)
        return Response({"response": True, "message": "Заказ в ожидании!"}, status=status.HTTP_201_CREATED)


class CallListView(generics.ListAPIView):
    queryset = Rental.objects.filter(status='request').order_by('-id')
    serializer_class = CallListSerializer


class AcceptCallView(generics.CreateAPIView):
    serializer_class = AcceptCallSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user.user_type == "driver":
            try:
                call = Rental.objects.get(pk=serializer.data["call_id"])
                if call.status == "request":
                    call.driver = request.user.driver
                    call.status = 'driver-accepted'
                    call.save()
                    return Response({"response": True, "message": "Заказ принят!"}, status=status.HTTP_201_CREATED)
                return Response({"response": False, "message": "Упс.. Вы не успели принять данный заказ"})
            except Rental.DoesNotExist:
                return Response({"response": False, "message": "Обьект не существует!"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response": False, "message": "Вы не являетесь таксистом!"}, status=status.HTTP_403_FORBIDDEN)