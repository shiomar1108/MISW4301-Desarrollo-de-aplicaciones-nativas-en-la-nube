from src.main import app
from faker import Faker
from datetime import datetime, timedelta

from test.mocks import (
    mock_post_route_success,
    mock_post_posts_success,
    mock_post_users_success,
    mock_post_offers_success,
    mock_post_scores_success,
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
                mock_post_route_success,
                mock_post_posts_success,
                mock_post_users_success,
                mock_post_offers_success,
                mock_post_scores_success,
                mock_post_rf005_success
                
            ):
                response = test_client.get(
                    "/rf005/posts/cb08a884-5118-11ee-b571-0242ac190005",                   
                    headers={"Authorization": f"Bearer 1fbb9f16-67f4-44c9-964a-6282210673d9"},
                )
        assert response.status_code == 201