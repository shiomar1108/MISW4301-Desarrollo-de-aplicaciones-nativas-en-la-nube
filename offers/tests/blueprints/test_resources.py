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
        self.fragile = random.choice([True, False])
        self.offer = self.dataFactory.pydecimal(left_digits=6, right_digits=2, positive=True)
        self.data = {
            "postId": f"{self.postId}",
            "userId": f"{self.userId}",
            "description": f"{self.description}",
            "size": f"{self.size}",
            "fragile": self.fragile,
            "offer": self.offer
        }
        self.token = self.dataFactory.sentence(nb_words=1)

    # Función que crea una oferta
    def execute_create_offer(self, data, headers):
        with app.test_client() as test_client:
            self.responseCreateOffer = test_client.post(
                '/offers', json=data, headers=headers
            )

    # Función que elimina una oferta
    def execute_delete_offer(self, headers):
        offerId = self.dataFactory.uuid4()
        with app.test_client() as test_client:
            self.responseDeleteOffer = test_client.delete(
                '/offers/'+offerId, headers=headers
            )

    # Función que regresa una oferta
    def execute_get_offer(self, headers):
        with app.test_client() as test_client:
            self.responseGetOffer = test_client.get(
                '/offers/'+self.postId, headers=headers
            )

    # Función que filtra y regresa una oferta sin parametros
    def execute_list_offers_noparam(self, headers):
        with app.test_client() as test_client:
            self.responseListOffer = test_client.get(
                '/offers', headers=headers
            )

    # Función que filtra y regresa una oferta con owner
    def execute_list_offers_owner(self, headers):
        with app.test_client() as test_client:
            self.responseListOffer = test_client.get(
                '/offers?owner=' + self.userId, headers=headers
            )

    # Función que filtra y regresa una oferta con post
    def execute_list_offers_post(self, headers):
        with app.test_client() as test_client:
            self.responseListOffer = test_client.get(
                '/offers?post=' + self.postId, headers=headers
            )

    # Función que filtra y regresa una oferta con post y owner
    def execute_list_offers_both(self, headers):
        with app.test_client() as test_client:
            self.responseListOffer = test_client.get(
                '/offers?post=' + self.postId + '&owner=' + self.userId, headers=headers
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

    # Función que valida la creacion de una oferta sin enviar el token
    def test_create_offer_without_token(self):
        self.set_up()
        headers = {}
        self.execute_create_offer(self.data, headers)
        response_json = json.loads(self.responseCreateOffer.data)
        assert self.responseCreateOffer.status_code == 403
        assert 'msg' in response_json
        assert response_json['msg'] == 'El token no está en el encabezado de la solicitud'

    # Función que valida la creacion exitosa de una oferta
    def test_create_offer(self):
        self.set_up()
        headers = {}
        headers["Authorization"] = f"Bearer {self.token}"
        self.data["offer"] = float(self.data["offer"])
        self.execute_create_offer(self.data, headers)
        json.loads(self.responseCreateOffer.data)
        assert self.responseCreateOffer.status_code == 201

    # Función que valida la eliminacion de una oferta sin enviar el token
    def test_delete_offer_without_token(self):
        self.set_up()
        headers = {}
        headers["Authorization"] = f"Bearer {self.token}"
        self.data["offer"] = float(self.data["offer"])
        self.execute_create_offer(self.data, headers)
        headers = {}
        self.execute_delete_offer(headers)
        response_json = json.loads(self.responseDeleteOffer.data)
        assert self.responseDeleteOffer.status_code == 403
        assert 'msg' in response_json
        assert response_json['msg'] == 'El token no está en el encabezado de la solicitud'

    # Función que valida la eliminacion de una oferta sin enviar el token
    def test_get_offer_without_token(self):
        self.set_up()
        headers = {}
        headers["Authorization"] = f"Bearer {self.token}"
        self.data["offer"] = float(self.data["offer"])
        self.execute_create_offer(self.data, headers)
        headers = {}
        self.execute_get_offer(headers)
        response_json = json.loads(self.responseGetOffer.data)
        assert self.responseGetOffer.status_code == 403
        assert 'msg' in response_json
        assert response_json['msg'] == 'El token no está en el encabezado de la solicitud'

    # Función que valida el filtrado de una oferta sin enviar el token
    def test_get_offer_without_token(self):
        self.set_up()
        headers = {}
        headers["Authorization"] = f"Bearer {self.token}"
        self.data["offer"] = float(self.data["offer"])
        self.execute_create_offer(self.data, headers)
        headers = {}
        self.execute_list_offers_noparam(headers)
        response_json = json.loads(self.responseListOffer.data)
        assert self.responseListOffer.status_code == 403
        assert 'msg' in response_json
        assert response_json['msg'] == 'El token no está en el encabezado de la solicitud'



