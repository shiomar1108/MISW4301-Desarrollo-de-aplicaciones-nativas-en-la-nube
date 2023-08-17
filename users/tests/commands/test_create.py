from src.commands.create import CreateUser
from faker import Faker

# Clase que contiene la logica de las pruebas del servicio
class TestCreate():
    
    dataFactory = Faker()
    
    # Función que valida la creación exitosa de un usuario
    def test_create_new_user(self):
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
        result = CreateUser(data).execute()
        assert result != None
    
    # Función que valida la creación de un usuario ya registrado    
    def test_existing_user_creation(self):
        try:
            existingUser = False
            # Creación nuevo usuario
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
            result = CreateUser(data).execute()
            assert result != None
            # Creación usuario existente
            result = CreateUser(data).execute()
        except Exception as e:
            assert e.code == 412
   
    # Función que valida la creación de un usuario cuando se envia un request invalido
    def test_create_user_bad_request(self):
        try:
            fullName = self.dataFactory.name()
            data = {
                "fullName": f"{fullName}"
            }
            # Creación usuario con data incompleta
            result = CreateUser(data).execute()
        except Exception as e:
            assert e.code == 400     
        
        
        
        
        
        