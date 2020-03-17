import requests


class BaseProvider:
    def __init__(self):
        self.session = requests.Session()

    def get_temp(self, lat, lon, unit=None) -> float:
        raise NotImplementedError

    @staticmethod
    def to_celsius(F):
        return (F - 32) * 5 / 9

    @staticmethod
    def to_fahrenheit(C):
        return (C * 9 / 5) + 32
