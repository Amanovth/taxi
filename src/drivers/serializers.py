from geopy.distance import distance
from rest_framework import serializers
from .models import Driver


class NearestDriversListSerializer(serializers.ModelSerializer):
    display_tariff = serializers.ReadOnlyField(source='car_tariff.tariff')
    distance_from_passenger = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = ['lon', 'lat', 'display_tariff', 'distance_from_passenger']

    def get_distance_from_passenger(self, obj):
        # Assuming 'lat' and 'lon' are fields in your Driver model
        passenger_latitude = self.context['request'].data.get('lat')
        passenger_longitude = self.context['request'].data.get('lon')

        # Calculate distance using the Haversine formula
        driver_location = (obj.lat, obj.lon)
        passenger_location = (float(passenger_latitude), float(passenger_longitude))
        distance_km = distance(driver_location, passenger_location).km
        return distance_km
