from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from apps.car.models import Car


class CarTestcase(APITestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        Car.objects.create(make="Volkswagen", model="Golf")
        self.create_user(self)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def create_user(self):
        self.client = APIClient()
        self.user = User(
            first_name="test_user",
            last_name="test",
            email="admin@gmail.com",
            username="admin",
            password="admin123",
        )
        self.user.set_password("admin123")
        self.user.save()
        self.token = Token.objects.create(user=self.user)

    def test_get_cars(self):
        response = self.client.get("http://127.0.0.1:8888/api/v1/cars/car/")
        self.assertEqual(int(response.status_code), 200)

    def test_post_car(self):
        url = "http://127.0.0.1:8888/api/v1/cars/car/"
        data = {"make": "bmw", "model": "x32"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_post_rate(self):
        car_id = Car.objects.get(make="Volkswagen").id
        url = "http://127.0.0.1:8888/api/v1/cars/rate/"
        data = {"car": car_id, "rating": 2}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_get_popular(self):
        response = self.client.get(
            "http://127.0.0.1:8888/api/v1/cars/popular/"
        )
        self.assertEqual(int(response.status_code), 200)

    def teardown_class(self):
        # Clean up after each test
        self.user.delete()
