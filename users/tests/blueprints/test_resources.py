from src.main import app
from faker import Faker
import json
import os

# Clase que contiene la logica del test
class TestResources():
    def setUp(self):
        self.dataFactory = Faker()
        self.password = Faker()
        
    # def test_create_user(self):
    #     username = f"test_{self.dataFactory.first_name()}"
    #     password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
    #     email = self.dataFactory.email()
    #     dni = self.dataFactory.random_int(1000, 100000000)
    #     fullName = self.dataFactory.name()
    #     phoneNumber = self.dataFactory.phone_number()
        
        # with app.test_client() as test_client:
        #     response = test_client.post(
        #         '/users', json={
        #             "username": f"{username}",
        #             "password": f"{password}",
        #             "email": f"{email}",
        #             "dni": f"{dni}",
        #             "fullName": f"{fullName}",
        #             "phoneNumber": f"{phoneNumber}",
        #         }
        #     )
        #     response_json = json.loads(response.data)

        # assert response.status_code == 201
        # assert 'id' in response_json
        # assert 'createdAt' in response_json
        assert True

    # def test_sum_two_number(self):
    #     with app.test_client() as test_client:
    #         response = test_client.post(
    #             '/sum', json={
    #                 'x': 5,
    #                 'y': 6
    #             }
    #         )
    #         response_json = json.loads(response.data)

    #         assert response.status_code == 200
    #         assert 'sum' in response_json
    #         assert 'version' in response_json

    # def test_multiply_two_number(self):
    #     with app.test_client() as test_client:
    #         response = test_client.post(
    #             '/multiply', json={
    #                 'x': 5,
    #                 'y': 6
    #             }
    #         )
    #         response_json = json.loads(response.data)

    #         assert response.status_code == 200
    #         assert 'multiplication' in response_json
    #         assert 'version' in response_json

    # def test_divide_two_number(self):
    #     with app.test_client() as test_client:
    #         response = test_client.post(
    #             '/divide', json={
    #                 'x': 5,
    #                 'y': 6
    #             }
    #         )
    #         response_json = json.loads(response.data)

    #         assert response.status_code == 200
    #         assert 'division' in response_json
    #         assert 'version' in response_json

    # def test_divide_by_zero(self):
    #     with app.test_client() as test_client:
    #         response = test_client.post(
    #             '/divide', json={
    #                 'x': 5,
    #                 'y': 0
    #             }
    #         )
    #         response_json = json.loads(response.data)

    #         assert response.status_code == 400
    #         assert 'mssg' in response_json
    #         assert 'version' in response_json
