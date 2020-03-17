from weather.providers import BaseProvider

from django.conf import settings


class WeatherDotComProvider(BaseProvider):
    BASE_URL = f"{settings.WEATHER_API_URL}/weatherdotcom"

    def __str__(self):
        return "weather.com"

    def get_temp(self, lat, lon, unit=None) -> float:
        response = self.session.post(
            self.BASE_URL, json={"lat": str(lat), "lon": str(lon)}
        )
        response.raise_for_status()

        data = response.json()

        # Assuming temperature always comes in Fahrenheit.
        assert data["query"]["results"]["channel"]["units"]["temperature"] == "F"

        temp = float(data["query"]["results"]["channel"]["condition"]["temp"])

        if unit == "celsius":
            return self.to_celsius(temp)

        return temp
