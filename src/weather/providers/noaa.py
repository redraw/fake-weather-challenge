from weather.providers import BaseProvider

from django.conf import settings


class NOAAProvider(BaseProvider):
    BASE_URL = f"{settings.WEATHER_API_URL}/noaa"

    def __str__(self):
        return "NOAA"

    def get_temp(self, lat, lon, unit=None) -> float:
        response = self.session.get(
            self.BASE_URL, params={"latlon": ",".join([str(lat), str(lon)])}
        )
        response.raise_for_status()

        data = response.json()
        temp = float(data["today"]["current"][unit])

        return temp
