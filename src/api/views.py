from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import TemperatureQuerySerializer
from weather.client import WeatherClient


class TemperatureView(APIView):
    """
    Calculate average temperature.
    
    Example JSON payload: 

    ```
    {
        "lat": 33.2
        "lon": 44.2,
        "filters": ["noaa", "accuweather"],
        "unit": "celsius"
    }
    ```
    
    - `unit` is optional. Possible values: `celsius`, `fahrenheit`
    """
    def post(self, request):
        serializer = TemperatureQuerySerializer(data=request.data)

        # Raise HTTP 400 with `serializer.errors` if serializer is not valid.
        serializer.is_valid(raise_exception=True)

        query = serializer.validated_data
        unit = query["unit"]

        weather = WeatherClient(providers=query["providers"])

        # Calculate average temperature.
        average_temp = weather.calculate_average_temp(
            lat=query["lat"], lon=query["lon"], unit=unit
        )

        return Response(data={"avg": {unit: average_temp}})
