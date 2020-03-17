from weather.providers import BaseProvider

from django.conf import settings


class AccuweatherProvider(BaseProvider):
    BASE_URL = f"{settings.WEATHER_API_URL}/accuweather"

    def __str__(self):
        return "Accuweather"

    def get_temp(self, lat, lon, unit=None) -> float:
        response = self.session.get(
            self.BASE_URL, params={"latitude": str(lat), "longitude": str(lon)}
        )
        response.raise_for_status()

        data = response.json()
        temp = float(data["simpleforecast"]["forecastday"][0]["current"][unit])

        return temp
