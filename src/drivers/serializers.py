from geopy.distance import distance
from rest_framework import serializers
from .models import Driver, Tariff


class NearestDriversListSerializer(serializers.ModelSerializer):
    display_tariff = serializers.ReadOnlyField(source='car_tariff.name')
    # distance_from_passenger = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = ['lat', 'lon', 'display_tariff', ]

    # def get_distance_from_passenger(self, obj):
    #     request_data = self.context['request'].data
    #     passenger_latitude = request_data.get('lat')
    #     passenger_longitude = request_data.get('lon')
    #
    #     if passenger_latitude is not None and passenger_longitude is not None:
    #         try:
    #             driver_location = (obj.lat, obj.lon)
    #             passenger_location = (float(passenger_latitude), float(passenger_longitude))
    #             distance_km = distance(driver_location, passenger_location).km
    #             return distance_km
    #         except ValueError as e:
    #             return None
    #     return None


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = "__all__"
