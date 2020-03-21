from rest_framework import serializers

from weather.client import WeatherClient


class TemperatureQuerySerializer(serializers.Serializer):
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)
    unit = serializers.ChoiceField(choices=["celsius", "fahrenheit"], default="celsius")
    providers = serializers.CharField(required=False)

    def validate_providers(self, value):
        providers = set()
        valid_providers = WeatherClient.PROVIDERS_MAP.keys()

        for key in value.split(","):
            if key not in valid_providers:
                raise serializers.ValidationError(f"Invalid provider: {key}")
            providers.add(key)

        return providers

    def validate_lat(self, value):
        if not (-90 <= value <= 90):
            raise serializers.ValidationError(f"Latitude out of range: {value}")
        return value

    def validate_lon(self, value):
        if not (-180 <= value <= 180):
            raise serializers.ValidationError(f"Longitude out of range: {value}")
        return value
