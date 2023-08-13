# Importación de dependencias
import traceback
from errors import ApiError, UserNameExists, UserEmailExists, BadRequest
from validators.validators import validateSchema, createUserSchema
from .base_command import BaseCommannd
from models import db, User
import sqlalchemy
import uuid
import hashlib

# Clase que contiene la logica de creción de usuarios
class CreateUser(BaseCommannd):
    def __init__(self, user):
        self.validateRequest(user)

    # Función que valida si existe un usuario con el username
    def validateUserName(self, username):
        userToConsult = User.query.filter(User.username == username).first()
        if userToConsult != None:
            raise UserNameExists

    # Función que valida si existe un usuario con el username
    def validateEmail(self, email):
        userToConsult = User.query.filter(User.email == email).first()
        if userToConsult != None:
            raise UserEmailExists

    # Función que valida si existe un usuario con el username
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
            self.dni = None           
        if "fullName" in userJson:
            self.fullName = userJson['fullName']
        else:
            self.fullName = None
        if "phoneNumber" in userJson:
            self.phoneNumber = userJson['phoneNumber']
        else:
            self.phoneNumber = None

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
                password=hashlib.sha512(self.password.encode(
                    'utf-8') + salt.encode('utf-8')).hexdigest(),
                salt=salt
            )
            db.session.add(newUser)
            db.session.commit()
            return newUser
        except sqlalchemy.exc.IntegrityError as e:
            traceback.print_exc()
            raise ApiError(e)
        
