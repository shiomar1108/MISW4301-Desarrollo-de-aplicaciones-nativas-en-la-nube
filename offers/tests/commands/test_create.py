import random
from src.commands.create import CreateOffer
from faker import Faker

# Clase que contiene la logica de las pruebas del servicio
class TestCreate():

    # Declaración constantes
    sizeList = ["LARGE", "MEDIUM", "SMALL"]
    dataFactory = Faker()
    postId = None
    userId = None
    description = None
    size = None
    fragile = None
    offer = None
    data = {}

    # Función que genera datos del la oferta
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

    # Función que valida la creación exitosa de una oferta
    def test_create_new_offer(self):
        # Creación oferta
        self.set_up()
        result = CreateOffer(self.data).execute()
        assert result != None

    # Función que valida la creación de una oferta con un parametro faltante
    def test_create_new_offer_missing(self):
        try:
            # Creación oferta
            self.set_up()
            data2 = {
            "postId": f"{self.postId}",
            "userId": f"{self.userId}",
            "description": f"{self.description}",
            "size": f"{self.size}",
            "fragile": f"{self.fragile}"
        }
            CreateOffer(data2).execute()
        except Exception as e:
            assert e.code == 400

    # Función que valida la creación de una oferta con un parametro mal
    def test_create_new_offer_missing(self):
        try:
            # Creación oferta
            self.set_up()
            data3 = {
            "postId": f"{self.postId}",
            "userId": f"{self.userId}",
            "description": f"{self.description}",
            "size": f"{self.size}",
            "fragile": f"{self.fragile}",
            "offer": f"{-100}"
        }
            CreateOffer(data3).execute()
        except Exception as e:
            assert e.code == 412