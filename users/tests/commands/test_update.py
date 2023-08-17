from faker import Faker
from src.commands.create import CreateUser
from src.commands.update import UpdateUser
import uuid

# Clase que contiene la logica de las pruebas del servicio
class TestUpdate():
    
    dataFactory = Faker()
    
    # Función que valida la actualización exitosa de un usuario
    def test_update_user(self):
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
        # Actualización información del usuario
        statusUpdate = "VERIFICADO"
        dniUpdate = str(self.dataFactory.random_int(1000, 100000000))
        fullNameUpdate = self.dataFactory.name()
        phoneNumberUpdate = str(self.dataFactory.random_int(1000000, 100000000000))
        dataUpdate = {
            "status": f"{statusUpdate}",
            "dni": f"{dniUpdate}",
            "fullName": f"{fullNameUpdate}",
            "phoneNumber": f"{phoneNumberUpdate}"
        }
        resultUpdate = UpdateUser(userId, dataUpdate).execute()
        assert resultUpdate.status == statusUpdate
        assert resultUpdate.dni == dniUpdate
        assert resultUpdate.fullName == fullNameUpdate
        assert resultUpdate.phoneNumber == phoneNumberUpdate

    # Función que valida el request vacio
    def test_update_user_empty_request(self):
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
            userId = result.id
            # Actualización información del usuario
            dataUpdate = {}
            UpdateUser(userId, dataUpdate).execute()
        except Exception as e:
            assert e.code == 400       

    # Función que valida los parametros de entrada
    def test_update_user_bad_request(self):
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
            userId = result.id
            # Actualización información del usuario
            emailUpdate = self.dataFactory.email()
            dataUpdate = {
                "email": f"{emailUpdate}"
            }
            UpdateUser(userId, dataUpdate).execute()
        except Exception as e:
            assert e.code == 400       

    # Función que valida la actualizacion de un usuario no registrado
    def test_update_user_non_existent(self):
        try:
            userId = uuid.uuid4()
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
            # Actualización de usuario no existente
            UpdateUser(userId, data).execute()
        except Exception as e:
            assert e.code == 404             
        
        
        
        
        