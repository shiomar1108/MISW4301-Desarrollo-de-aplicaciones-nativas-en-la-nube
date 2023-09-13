from src.main import app
from faker import Faker
from datetime import datetime, timedelta

from test.mocks import ( 
    mock_post_rf005_success
)
from faker.providers import DynamicProvider
from httmock import HTTMock
from uuid import uuid4
import json



# Clase que contiene la logica del test
class TestRF005Resources:


    def test_rf005_success(self):
        # Verificacion de Happy Path        
        with app.test_client() as test_client:
            with HTTMock(                               
                mock_post_rf005_success
                
            ):
                response = test_client.get(
                    "/rf005/posts/7db2089e-51e7-11ee-a25b-0242ac120005"                   
                    
                )
        assert response.status_code == 201