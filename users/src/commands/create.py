# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError, UserNameExists, UserEmailExists
from validators.validators import validateSchema, createUserSchema
from models.models import db, User
from sqlalchemy.exc import SQLAlchemyError
import uuid
import hashlib
import traceback

# Clase que contiene la logica de creción de usuarios
class CreateUser(BaseCommannd):
    def __init__(self, user):
        self.validateRequest(user)

    # Función que valida si existe un usuario con el username
    def validateUserName(self, username):
        userToConsult = User.query.filter(User.username == username).first()
        if userToConsult != None:
            raise UserNameExists

    # Función que valida si existe un usuario con el email
    def validateEmail(self, email):
        userToConsult = User.query.filter(User.email == email).first()
        if userToConsult != None:
            raise UserEmailExists# pragma: no cover

    # Función que permite generar el password
    def generatePassword(self, salt):
        return hashlib.sha512(self.password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

    # Función que valida el request del servicio
    def validateRequest(self, userJson):
        # Validacion del request
        validateSchema(userJson, createUserSchema)
        # Asignacion de variables
        self.username = userJson['username']
        self.password = userJson['password']
        self.email = userJson['email']
        if "dni" in userJson:
            self.dni = userJson['dni'] 
        else:
            self.dni = None# pragma: no cover
        if "fullName" in userJson:
            self.fullName = userJson['fullName']
        else:
            self.fullName = None# pragma: no cover
        if "phoneNumber" in userJson:
            self.phoneNumber = userJson['phoneNumber']
        else:
            self.phoneNumber = None# pragma: no cover

    # Función que realiza creación del usuario
    def execute(self):
        try:
            self.validateUserName(self.username)
            self.validateEmail(self.email)
            salt = uuid.uuid4().hex
            newUser = User(
                username=self.username,
                email=self.email,
                phoneNumber=self.phoneNumber,
                dni=self.dni,
                fullName=self.fullName,
                password=self.generatePassword(salt),
                salt=salt
            )
            db.session.add(newUser)
            db.session.commit()
            return newUser
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
        
