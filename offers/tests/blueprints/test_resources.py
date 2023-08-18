import random
from src.main import app
from faker import Faker
import json

# Clase que contiene la logica del test
class TestResources():

    # Declaración constantes
    sizeList = ["LARGE", "MEDIUM", "SMALL"]
    dataFactory = Faker()
    offerId = None
    postId = None
    userId = None
    description = None
    size = None
    fragile = None
    offer = None
    responseCreateOffer = {}
    responseDeleteOffer = {}
    responseGetOffer = {}
    responseListOffer = {}
    data = {}  

    # Función que genera datos del la offerta
    def set_up(self):
        self.postId = self.dataFactory.uuid4()
        self.userId = self.dataFactory.uuid4()
        self.description = self.dataFactory.sentence(nb_words=8)
        self.size = random.choice(self.sizeList)
        self.fragile = self.dataFactory.pybool(left_digits=6, right_digits=2, positive=True)
        self.offer = self.dataFactory.pydecimal()
        self.data = {
            "postId": f"{self.postId}",
            "userId": f"{self.userId}",
            "description": f"{self.description}",
            "size": f"{self.size}",
            "fragile": f"{self.fragile}",
            "offer": f"{self.offer}"
        }

    # Función que crea una oferta
    def execute_create_offer(self, data):
        with app.test_client() as test_client:
            self.responseCreateOffer = test_client.post(
                '/offers', json=data
            )

    # Función que elimina una oferta
    def execute_delete_offer(self):
        with app.test_client() as test_client:
            self.responseDeleteOffer = test_client.delete(
                '/offers/'+self.postId
            )

    # Función que regresa una oferta
    def execute_get_offer(self):
        with app.test_client() as test_client:
            self.responseGetOffer = test_client.get(
                '/offers/'+self.postId
            )

    # Función que filtra y regresa una oferta sin parametros
    def execute_list_offers_noparam(self):
        with app.test_client() as test_client:
            self.responseListOffer = test_client.get(
                '/offers'
            )

    # Función que filtra y regresa una oferta con owner
    def execute_list_offers_owner(self):
        with app.test_client() as test_client:
            self.responseListOffer = test_client.get(
                '/offers?owner=' + self.userId
            )

    # Función que filtra y regresa una oferta con post
    def execute_list_offers_post(self):
        with app.test_client() as test_client:
            self.responseListOffer = test_client.get(
                '/offers?post=' + self.postId
            )

    # Función que filtra y regresa una oferta con post y owner
    def execute_list_offers_both(self):
        with app.test_client() as test_client:
            self.responseListOffer = test_client.get(
                '/offers?post=' + self.postId + '&owner=' + self.userId
            )

    # Función que valida el estado del servidor
    def test_health_check(self):
        # Reset tabla usuarios
        with app.test_client() as test_client:
            response = test_client.get(
                '/offers/ping'
            )
            data = str(response.data)
        assert response.status_code == 200
        assert 'pong' in data

    # Función que limpia todos los usuarios registrados
    def test_reset_offers(self):
        # Reset tabla usuarios
        data = {}
        with app.test_client() as test_client:
            response = test_client.post(
                '/offers/reset', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'msg' in response_json
        assert response_json['msg'] == 'Todos los datos fueron eliminados'
