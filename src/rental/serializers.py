from rest_framework import serializers
from .models import Rental
from rest_framework import serializers


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = [
            "tarif",
            "lat_a",
            "lon_a",
            "lat_b",
            "lon_b",
            "total_cost",
            "payment_type",
        ]


class CallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = [
            "id",
            "tarif",
            "passenger",
            "point_a_street",
            "lat_a",
            "lon_a",
            "point_b_street",
            "lat_b",
            "lon_b",
            "total_cost",
            "payment_type",
        ]


class AcceptCallSerializer(serializers.ModelSerializer):
    call_id = serializers.IntegerField()

    class Meta:
        model = Rental
        fields = ["call_id"]


class HistorySerializers(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    time_of_day = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = Rental
        fields = [
            "id",
            "date",
            "time_of_day",
            "text",
        ]

    def get_date(self, obj):
        if obj.time_start:
            return obj.time_start.strftime('%d %B, %A')
        
    def get_time_of_day(self, obj):
        if obj.time_start is None:
            return "Time information is missing."

        current_hour = int(obj.time_start.strftime("%H"))

        if 5 <= current_hour < 10:
            return f"Поездка утром в {obj.time_start.strftime('%H:%M')}"
        elif 10 <= current_hour < 18:
            return f"Поездка днем в {obj.time_start.strftime('%H:%M')}"
        elif 18 <= current_hour < 22:
            return f"Поездка вечером в {obj.time_start.strftime('%H:%M')}"
        else:
            return f"Поездка ночью в {obj.time_start.strftime('%H:%M')}"
        
    def get_text(self, obj):
        if obj.status == 'completed':
            return f'{obj.total_cost} сом, {obj.point_a_street} {obj.point_b_street}'

class HistoryDetailSerializers(serializers.ModelSerializer):
    star = serializers.SerializerMethodField()
    time_of_day = serializers.SerializerMethodField()
    driver_photo = serializers.SerializerMethodField()
    car = serializers.SerializerMethodField()
    car_color = serializers.SerializerMethodField()
    number_auto = serializers.SerializerMethodField()

    class Meta:
        model = Rental
        fields = [
            "id",
            "time_of_day",
            "time_start",
            "status",
            "total_cost",
            "lat_a",
            "lon_a",
            "lat_b",
            "lon_b",
            "star",
            "driver_photo",
            "car",
            "car_color",
            "number_auto",
        ]

    def get_star(self, obj):
        if obj.driver:
            return obj.driver.star
        return None

    def get_time_of_day(self, obj):
        if obj.time_start is None:
            return "Time information is missing."

        current_hour = int(obj.time_start.strftime("%H"))

        if 5 <= current_hour < 10:
            return f"Поездка утром в {obj.time_start.strftime('%H:%M')}"
        elif 10 <= current_hour < 18:
            return f"Поездка днем в {obj.time_start.strftime('%H:%M')}"
        elif 18 <= current_hour < 22:
            return f"Поездка вечером в {obj.time_start.strftime('%H:%M')}"
        else:
            return f"Поездка ночью в {obj.time_start.strftime('%H:%M')}"

    def get_driver_photo(self, obj):
        if obj.driver.driver_photo:
            return f"http://213.171.5.5{obj.driver.driver_photo.url}"
        return None

    def get_car(self, obj):
        if obj.driver.car_brand:
            return f'{obj.driver.car_brand} {obj.driver.car_model}'
        return None

    def get_car_color(self, obj):
        if obj.driver.car_color:
            return obj.driver.car_color
        return None

    def get_number_auto(self, obj):
        if obj.driver.number_auto:
            return obj.driver.number_auto
        return None
