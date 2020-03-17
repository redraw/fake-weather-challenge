from django.test import TestCase
from rest_framework.test import APITestCase


class TestTemperatureView(APITestCase):
    def test_required_fields(self):
        response = self.client.post("/api/temp/", data={})
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertEqual(data["lat"], ["This field is required."])
        self.assertEqual(data["lon"], ["This field is required."])
