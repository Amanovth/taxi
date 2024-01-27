from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import (
    RegisterSerializer,
    VerifyPhoneSerializer,
    UpdateFullNameSerializer,
    LoginSerializer,
)
from .models import User
from .services import send_sms


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            phone = serializer.validated_data.get('phone')

            try:
                user = User.objects.get(phone=phone)
                user.activated = False
                user.save()
            except ObjectDoesNotExist:
                user = User(phone=phone)
                user.save()

            # sms_sent = send_sms(phone, "Подтвердите номер телефона", user.code)

            # if sms_sent:
            return Response(
                {
                    "response": True,
                    "message": _("Код подтверждения был отправлен на ваш номер."),
                },
                status=status.HTTP_201_CREATED,
            )
            # return Response(
            #     {"response": False, "message": _("Something went wrong!")},
            #     status=status.HTTP_400_BAD_REQUEST,
            # )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPhoneView(generics.GenericAPIView):
    serializer_class = VerifyPhoneSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.data['code']
            phone = serializer.data['phone']

            try:
                user = User.objects.get(phone=phone)

                if user.code == code:
                    user.activated = True
                    user.save()

                    token, created = Token.objects.get_or_create(user=user)

                    return Response(
                        {
                            'response': True,
                            # 'message': _('Пользователь успешно зарегистрирован.'),
                            'token': token.key,
                        }
                    )
                return Response(
                    {'response': False, 'message': _('Введен неверный код')}
                )
            except ObjectDoesNotExist:
                return Response(
                    {
                        'response': False,
                        'message': _('Пользователь с таким телефоном не существует'),
                    }
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class UpdateFullNameView(generics.UpdateAPIView):
    serializer_class = UpdateFullNameSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            token = Token.objects.get(user=user)
            token.delete()
            return Response({'response': True})
        except ObjectDoesNotExist:
            return Response({'response': False}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            phone = request.data.get("phone")
            password = request.data.get("password")

            try:
                get_user = User.objects.get(phone=phone)
            except ObjectDoesNotExist:
                return Response(
                    {
                        "response": False,
                        "message": "Пользователь с указанным телефонным номером уже существует",
                    }
                )

            user = authenticate(request, phone=phone, password=password)

            if not user:
                return Response(
                    {
                        "response": False,
                        "message": "Невозможно войти в систему с указанным номером телефона",
                    }
                )

            if user.is_verified:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "response": True,
                        "isactivated": True,
                        "token": token.key,
                        "phone": user.phone,
                    }
                )
        
        return Response(serializer.errors)
