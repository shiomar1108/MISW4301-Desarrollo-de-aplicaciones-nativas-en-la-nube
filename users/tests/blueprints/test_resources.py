import uuid
from src.main import app
from faker import Faker
import json

# Clase que contiene la logica del test
class TestResources():

    dataFactory = Faker()
        
    # Función que valida la creación exitosa de un usuario
    def test_create_new_user(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        
    # Función que valida la creación de un usuario ya registrado    
    def test_existing_user_creation(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        # Creación usuario existente
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 412
        assert 'msg' in response_json
        assert response_json['msg'] == 'El username ya se encuentra registrado' 

    # Función que valida la creación de un usuario cuando se envia un request invalido   
    def test_create_user_bad_request(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
                "fullName": f"{fullName}"
            }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 400
        assert 'msg' in response_json
        assert response_json['msg'] == 'Párametros de entrada invalidos'         
           
    # Función que valida la actualización exitosa de un usuario
    def test_update_user(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        userId = response_json['id']
        # Actualización de usuario
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
        with app.test_client() as test_client:
            response = test_client.patch(
                f'/users/{userId}', json=dataUpdate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'msg' in response_json
        assert response_json['msg'] == 'el usuario ha sido actualizado' 
        
    # Función que valida el request vacio
    def test_update_user_empty_request(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        userId = response_json['id']
        # Actualización de usuario
        dataUpdate = {}
        with app.test_client() as test_client:
            response = test_client.patch(
                f'/users/{userId}', json=dataUpdate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 400
        assert 'msg' in response_json
        assert response_json['msg'] == 'Párametros de entrada invalidos'         
        
    # Función que valida los parametros de entrada
    def test_update_user_bad_request(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        userId = response_json['id']
        # Actualización de usuario
        emailUpdate = self.dataFactory.email()
        dataUpdate = {
                "email": f"{emailUpdate}"
            }
        with app.test_client() as test_client:
            response = test_client.patch(
                f'/users/{userId}', json=dataUpdate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 400
        assert 'msg' in response_json
        assert response_json['msg'] == 'Párametros de entrada invalidos'         

    # Función que valida la actualizacion de un usuario no registrado
    def test_update_user_non_existent(self):
        userId = uuid.uuid4()
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 100000))
        password = self.dataFactory.password(
            length=10, special_chars=False, upper_case=True, lower_case=True, digits=True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        dataUpdate = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.patch(
                f'/users/{userId}', json=dataUpdate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 404
        assert 'msg' in response_json
        assert response_json['msg'] == 'El usuario no se encuentra registrado'          
        
    # Función que valida la generación exitosa del token
    def test_generate_token(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        userId = response_json['id']
        # Generación token
        dataAuthenticate = {
            "username": f"{username}",
            "password": f"{password}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/auth', json=dataAuthenticate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'id' in response_json
        assert 'expireAt' in response_json
        assert 'token' in response_json
        assert response_json['id'] == userId

    # Función que valida la generación del token con credenciales erroneas
    def test_generate_token_wrong_credentials(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        userId = response_json['id']
        # Generación token
        dataAuthenticate = {
            "username": f"{username}",
            "password": f"{password}wrong"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/auth', json=dataAuthenticate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 404
        assert 'msg' in response_json
        assert response_json['msg'] == 'El password es incorrecto'   

    # Función que valida la generación del token con un request invalido
    def test_generate_token_bad_request(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        userId = response_json['id']
        # Generación token
        dataAuthenticate = {
            "username": f"{username}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/auth', json=dataAuthenticate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 400
        assert 'msg' in response_json
        assert response_json['msg'] == 'Párametros de entrada invalidos'          
        
    # Función que valida la generación del token con un usuario no existente
    def test_generate_token_user_non_existent(self):        
        # Generación token
        dataAuthenticate = {
                "username": "fake",
                "password": "fake"
            }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/auth', json=dataAuthenticate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 404
        assert 'msg' in response_json
        assert response_json['msg'] == 'El usuario no se encuentra registrado'
        
    # Función que limpia todos los usuarios registrados
    def test_reset_users(self):
        # Reset tabla usuarios
        data = {}
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/reset', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'msg' in response_json
        assert response_json['msg'] == 'Todos los datos fueron eliminados'
        
    # Función que valida el estado del servidor
    def test_health_check(self):
        # Reset tabla usuarios
        with app.test_client() as test_client:
            response = test_client.get(
                '/users/ping'
            )
            data = str(response.data)
        assert response.status_code == 200
        assert 'pong' in data
        
    # Función que consulta exitosamente el detalle del usuario
    def test_detail_user(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        userId = response_json['id']
        # Generación token
        dataAuthenticate = {
            "username": f"{username}",
            "password": f"{password}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/auth', json=dataAuthenticate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'id' in response_json
        assert 'expireAt' in response_json
        assert 'token' in response_json
        assert response_json['id'] == userId
        token = response_json['token']
        # Consulta de usuario
        headers = {}
        headers["Authorization"] = f"Bearer {token}"
        with app.test_client() as test_client:
            response = test_client.get(
                '/users/me', headers=headers
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert response_json["id"] == userId
        assert response_json["username"] == username
        assert response_json["email"] == email
        assert response_json["fullName"] == fullName
        assert response_json["dni"] == dni
        assert response_json["phoneNumber"] == phoneNumber
        assert response_json["status"] == "NO_VERIFICADO"

    # Función que valida la consulta del usuario sin enviar el token
    def test_detail_user_without_token(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        userId = response_json['id']
        # Generación token
        dataAuthenticate = {
            "username": f"{username}",
            "password": f"{password}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/auth', json=dataAuthenticate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'id' in response_json
        assert 'expireAt' in response_json
        assert 'token' in response_json
        assert response_json['id'] == userId
        # Consulta de usuario
        headers = {}
        with app.test_client() as test_client:
            response = test_client.get(
                '/users/me', headers=headers
            )
            response_json = json.loads(response.data)
        assert response.status_code == 403
        assert 'msg' in response_json
        assert response_json['msg'] == 'El token no está en el encabezado de la solicitud'
        
    # Función que valida la consulta del usuario enviando un token invalido
    def test_detail_user_invalid_token(self):
        username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        password = self.dataFactory.password(length=10, special_chars=False, upper_case=True, lower_case= True, digits= True)
        email = self.dataFactory.email()
        dni = str(self.dataFactory.random_int(1000, 100000000))
        fullName = self.dataFactory.name()
        phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        # Creación nuevo usuario
        data = {
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}",
            "dni": f"{dni}",
            "fullName": f"{fullName}",
            "phoneNumber": f"{phoneNumber}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json
        # Generación token
        dataAuthenticate = {
            "username": f"{username}",
            "password": f"{password}"
        }
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/auth', json=dataAuthenticate
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'id' in response_json
        assert 'expireAt' in response_json
        assert 'token' in response_json
        token = response_json['token']
        # Consulta de usuario
        headers = {}
        headers["Authorization"] = f"Bearer {token}fake"
        with app.test_client() as test_client:
            response = test_client.get(
                '/users/me', headers=headers
            )
            response_json = json.loads(response.data)
        assert response.status_code == 401
        assert 'msg' in response_json
        assert response_json['msg'] == 'El token no es válido o está vencido'