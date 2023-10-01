import unittest
import requests
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, Base, Car

class CarInfoAPITest(unittest.TestCase):
    API_URL = "http://localhost/cars/"

    def setUp(self):
        ...

    def test_create_car(self):
        car = {
            "make": "Toyota",
            "model": "Corolla",
            "year": 2010
        }
        response = requests.post(self.API_URL, json=car)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["make"], "Toyota")
        self.assertEqual(response.json()["model"], "Corolla")
        self.assertEqual(response.json()["year"], 2010)

    def test_get_car(self):
        car = Car(make="Toyota", model="Corolla", year=2010)
        self.db.add(car)
        self.db.commit()
        car_id = car.id
        response = requests.get(self.API_URL + str(car_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], car_id)

    def test_invalid_car_id(self):
        car_id = 99999
        response = requests.get(self.API_URL + str(car_id))
        self.assertEqual(response.status_code, 404)

    def test_invalid_car_data(self):
        car = {
            "make": "Toyota",
            "year": "red"
        }
        response = requests.post(self.API_URL, json=car)
        self.assertEqual(response.status_code, 422)

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()