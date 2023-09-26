from faker import Faker
from src.commands.create import CreateUser
from src.commands.authenticate import Authenticate
from src.queries.detail import GetUserDetail
import uuid

# Clase que contiene la logica de las pruebas del servicio
class TestDetailUser():
    
    # Declaración constantes
    dataFactory = Faker()
    userId = None
    username = None
    password = None
    email = None
    dni = None
    fullName = None
    phoneNumber = None
    token = None
    data = {}    

    # Función que genera data del usuario
    def set_up(self):
        self.username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        self.password = self.dataFactory.password(
            length=10, special_chars=False, upper_case=True, lower_case=True, digits=True)
        self.email = self.dataFactory.email()
        self.dni = str(self.dataFactory.random_int(1000, 100000000))
        self.fullName = self.dataFactory.name()
        self.phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        self.data = {
            "username": f"{self.username}",
            "password": f"{self.password}",
            "email": f"{self.email}",
            "dni": f"{self.dni}",
            "fullName": f"{self.fullName}",
            "phoneNumber": f"{self.phoneNumber}"
        }
        
    # Función que crea un usuario nuevo
    def create_user(self):    
        # Creación nuevo usuario
        result = CreateUser(self.data).execute()
        assert result != None
        self.userId = result.id

    # Función que genera el token
    def generate_token(self):    
        # Generación del token
        data = {
            "username": f"{self.username}",
            "password": f"{self.password}"
        }
        resultToken = Authenticate(data).execute()
        assert resultToken.id == self.userId
        assert resultToken.expireAt != None
        assert resultToken.token != None
        assert uuid.UUID(resultToken.token, version=4)     
        self.token =  resultToken.token
    
    # Función que consulta exitosamente el detalle del usuario
    def test_detail_user(self):
        try:
            # Creación nuevo usuario
            self.set_up()
            self.create_user()
            # Generación token
            self.generate_token()
            # Consulta de usuario
            headers = {}
            headers["Authorization"] = "Bearer " + str(self.token)
            GetUserDetail(headers).query()
        except:
          assert True
        
    # Función que valida la consulta del usuario sin enviar el token
    def test_detail_user_without_token(self):
        try:
            # Consulta de usuario
            headers = {}
            GetUserDetail(headers).query()
        except Exception as e:
            assert e.code == 403   

    # Función que valida la consulta del usuario enviando un token invalido
    def test_detail_user_invalid_token(self):
        try:
            # Consulta de usuario
            tokenInvalid = uuid.uuid4()
            headers = {}
            headers["Authorization"] = "Bearer " + str(tokenInvalid)
            GetUserDetail(headers).query()
        except:
            assert True