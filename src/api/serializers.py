from rest_framework import serializers


class TemperatureQuerySerializer(serializers.Serializer):
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)
    providers = serializers.MultipleChoiceField(
        choices=["noaa", "weather.com", "accuweather"]
    )
