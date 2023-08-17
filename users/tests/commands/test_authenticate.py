from faker import Faker
from src.commands.create import CreateUser
from src.commands.authenticate import Authenticate
import uuid

# Clase que contiene la logica de las pruebas del servicio
class TestAuthenticate():
    
    dataFactory = Faker()
    
    # Función que valida la generación exitosa del token
    def test_generate_token(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(
            length=10, special_chars=False, upper_case=True, lower_case=True, digits=True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        # Creación nuevo usuario
        result = CreateUser(data).execute()
        assert result != None
        userId = result.id
        # Generación token
        data = {
            "username": f"{username}",
            "password": f"{password}"
        }
        resultUpdate = Authenticate(data).execute()
        assert resultUpdate.id == userId
        assert resultUpdate.expireAt != None
        assert resultUpdate.token != None
        assert uuid.UUID(resultUpdate.token, version=4)

    # Función que valida la generación del token con credenciales erroneas
    def test_generate_token_wrong_credentials(self):
        try:
            username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 100000))
            password = self.dataFactory.password(
                length=10, special_chars=False, upper_case=True, lower_case=True, digits=True)
            email = self.dataFactory.email()
            dni = str(self.dataFactory.random_int(1000, 100000000))
            fullName = self.dataFactory.name()
            phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
            data = {
                "username": f"{username}",
                "password": f"{password}",
                "email": f"{email}",
                "dni": f"{dni}",
                "fullName": f"{fullName}",
                "phoneNumber": f"{phoneNumber}"
            }
            # Creación nuevo usuario
            result = CreateUser(data).execute()
            assert result != None
            # Generación token
            data = {
                "username": f"{username}",
                "password": f"{password}wrong"
            }
            Authenticate(data).execute()
        except Exception as e:
            assert e.code == 404   

    # Función que valida la generación del token con un request invalido
    def test_generate_token_bad_request(self):
        try:
            username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 100000))
            password = self.dataFactory.password(
                length=10, special_chars=False, upper_case=True, lower_case=True, digits=True)
            email = self.dataFactory.email()
            dni = str(self.dataFactory.random_int(1000, 100000000))
            fullName = self.dataFactory.name()
            phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
            data = {
                "username": f"{username}",
                "password": f"{password}",
                "email": f"{email}",
                "dni": f"{dni}",
                "fullName": f"{fullName}",
                "phoneNumber": f"{phoneNumber}"
            }
            # Creación nuevo usuario
            result = CreateUser(data).execute()
            assert result != None
            # Generación token
            data = {
                "username": f"{username}"
            }
            Authenticate(data).execute()
        except Exception as e:
            assert e.code == 400    

    # Función que valida la generación del token con un usuario no existente
    def test_generate_token_user_non_existent(self):
        try:
            # Generación token
            data = {
                "username": "fake",
                "password": "fake"
            }
            Authenticate(data).execute()
        except Exception as e:
            assert e.code == 404  