from src.commands.create import CreatePost
from faker import Faker
from datetime import datetime, timedelta
from src.main import app
import requests
import uuid
import json
import os


class TestCreate():
    
    def set_up(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.username = self.data_factory.first_name() + str(self.data_factory.random_int(1, 1000000))
        self.password = self.data_factory.password(length=10, special_chars=False, upper_case=True, lower_case=True, digits=True)
        self.email = self.data_factory.email()
        self.dni = str(self.data_factory.random_int(1000, 100000000))
        self.fullName = self.data_factory.name()
        self.phoneNumber = str(self.data_factory.random_int(1000000, 100000000000))
        new_user = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "dni": self.dni,
            "fullName": self.fullName,
            "phoneNumber": self.phoneNumber
        }
        request_creation = self.client.post("/users", data=json.dumps(new_user), headers={"Content-Type": "application/json"},)
        assert request_creation.status_code == 200



    def test_create_new_post(self):
        self.set_up()
        pass