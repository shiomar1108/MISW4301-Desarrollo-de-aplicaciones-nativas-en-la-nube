from src.main import app
from faker import Faker
from datetime import datetime, timedelta

from test.mocks import (
    mmock_post_route_success,
    mock_post_posts_success,
    mock_post_users_success,
    mock_post_offers_success,
    mock_post_scores_success
)
from faker.providers import DynamicProvider
from httmock import HTTMock
from uuid import uuid4
import json



# Clase que contiene la logica del test
class TestRF005Resources:


    def test_rf005_success(self):
        # Verificacion de Happy Path
        self.set_up_working()
        with app.test_client() as test_client:
            with HTTMock(
                mock_post_route_success,
                mock_post_posts_success,
                mock_post_users_success,
                mock_post_offers_success,
                mock_post_scores_success,
                
            ):
                response = test_client.post(
                    "/rf005/posts/"+uuid4(),                   
                    headers={"Authorization": f"Bearer {uuid4()}"},
                )
        assert response.status_code == 201