from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import TemperatureQuerySerializer


class TemperatureView(APIView):
    def post(self, request):
        serializer = TemperatureQuerySerializer(data=request.data)

        # Raise HTTP 400 with `serializer.errors` if serializer is not valid.
        serializer.is_valid(raise_exception=True)

        return Response(data=serializer.validated_data)
