from unittest import mock

from django.test import TestCase
from rest_framework.test import APITestCase

from weather.exceptions import WeatherProviderError


class TestTemperatureView(APITestCase):
    PATH = "/api/temp/"

    def test_required_fields(self):
        response = self.client.get(self.PATH, {})
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertEqual(data["lat"], ["This field is required."])
        self.assertEqual(data["lon"], ["This field is required."])

    def test_invalid_coords(self):
        cases = [
            ("lat", "90", True),
            ("lat", "100", False),
            ("lat", "-90", True),
            ("lat", "-100", False),
            ("lon", "180", True),
            ("lon", "190", False),
            ("lon", "-180", True),
            ("lon", "-190", False)
        ]

        for case in cases:
            coord, value, valid = case
            with self.subTest(msg=case):
                response = self.client.get(self.PATH, {coord: value})
                self.assertEqual(response.status_code, 400)
                errors = response.json()
                self.assertEqual(coord not in errors.keys(), valid)

    def test_invalid_provider(self):
        response = self.client.get(self.PATH, {"providers": ["noaa", "asdf"]})
        self.assertEqual(response.status_code, 400)
        errors = response.json()
        self.assertIn("providers", errors)

    @mock.patch("weather.client.WeatherClient.calculate_average_temp")
    def test_weather_api_request_exception(self, mock_average_temp):
        mock_average_temp.side_effect = WeatherProviderError
        response = self.client.get(self.PATH, {"lat": 33.2, "lon": 44.3})
        self.assertEqual(response.status_code, 503)
