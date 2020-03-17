import logging
from statistics import mean

from weather.providers import NOAAProvider, AccuweatherProvider, WeatherDotComProvider
from weather.exceptions import WeatherProviderError

logger = logging.getLogger(__name__)


class WeatherClient:
    PROVIDERS_MAP = {
        "noaa": NOAAProvider,
        "accuweather": AccuweatherProvider,
        "weatherdotcom": WeatherDotComProvider,
    }

    def __init__(self, providers=None):
        providers = providers or self.PROVIDERS_MAP.keys()

        self.providers = [self.PROVIDERS_MAP[provider]() for provider in providers]

    def calculate_average_temp(self, lat, lon, unit=None) -> float:
        values = []

        for provider in self.providers:
            try:
                temp = provider.get_temp(lat, lon, unit=unit)
                values.append(temp)
            except Exception as e:
                logger.error(f"[{provider}] {str(e)}")

        if not values:
            raise WeatherProviderError(
                "We couldn't get the temperature of any chosen provider."
            )

        return mean(values)
