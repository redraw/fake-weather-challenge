from rest_framework import serializers

from weather.client import WeatherClient


class TemperatureQuerySerializer(serializers.Serializer):
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)
    unit = serializers.ChoiceField(choices=["celsius", "fahrenheit"], default="celsius")
    providers = serializers.MultipleChoiceField(
        choices=list(WeatherClient.PROVIDERS_MAP.keys())
    )
