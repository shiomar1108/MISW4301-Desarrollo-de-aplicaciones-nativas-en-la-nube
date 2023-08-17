from faker import Faker
from src.commands.create import CreateUser
from src.commands.authenticate import Authenticate
from src.queries.detail import GetUserDetail
import uuid

# Clase que contiene la logica de las pruebas del servicio
class TestDetailUser():
    
    dataFactory = Faker()
    
    # Función que consulta exitosamente el detalle del usuario
    def test_detail_user(self):
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
        resultToken = Authenticate(data).execute()
        assert resultToken.id == userId
        assert resultToken.expireAt != None
        assert resultToken.token != None
        assert uuid.UUID(resultToken.token, version=4)
        # Consulta de usuario
        headers = {}
        headers["Authorization"] = "Bearer " + str(resultToken.token)
        userDetail = GetUserDetail(headers).query()
        assert userDetail.id == userId
        assert userDetail.username == username
        assert userDetail.email == email
        assert userDetail.fullName == fullName
        assert userDetail.dni == dni
        assert userDetail.phoneNumber == phoneNumber
        assert userDetail.status == "NO_VERIFICADO"
        
    # Función que valida la consulta del usuario sin enviar el token
    def test_detail_user_without_token(self):
        try:
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
            resultToken = Authenticate(data).execute()
            assert resultToken.id == userId
            assert resultToken.expireAt != None
            assert resultToken.token != None
            assert uuid.UUID(resultToken.token, version=4)
            # Consulta de usuario
            headers = {}
            GetUserDetail(headers).query()
        except Exception as e:
            assert e.code == 403   

    # Función que valida la consulta del usuario enviando un token invalido
    def test_detail_user_invalid_token(self):
        try:
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
            
            # Consulta de usuario
            tokenInvalid = uuid.uuid4()
            headers = {}
            headers["Authorization"] = "Bearer " + str(tokenInvalid)
            GetUserDetail(headers).query()
        except Exception as e:
            assert e.code == 401  