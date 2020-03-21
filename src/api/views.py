from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import TemperatureQuerySerializer
from weather.client import WeatherClient
from weather.exceptions import WeatherProviderError


class TemperatureView(APIView):
    """
    Calculate average temperature.
    
    Available GET parameters:

    - `lat`: latitude
    - `lon`: longitude
    - `providers`: separated by comma. Possible values: `noaa`, `accuweather`, `weatherdotcom`
    - `unit`: default is `celsius`. Possible values: `celsius`, `fahrenheit`
    """

    def get(self, request):
        serializer = TemperatureQuerySerializer(data=request.query_params)

        # Raise HTTP 400 with `serializer.errors` if serializer is not valid.
        serializer.is_valid(raise_exception=True)

        query = serializer.validated_data
        unit = query["unit"]
        providers = query.get("providers")

        weather = WeatherClient(providers=providers)

        # Calculate average temperature.
        try:
            average_temp = weather.calculate_average_temp(
                lat=query["lat"], lon=query["lon"], unit=unit
            )
        except WeatherProviderError as error:
            return Response(
                status=status.HTTP_503_SERVICE_UNAVAILABLE, data={"message": str(error)}
            )

        return Response(data={"avg": {unit: average_temp}, "query": query})
