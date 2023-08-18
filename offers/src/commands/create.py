# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError
from validators.validators import validateSchema, createOfferSchema
from models.models import db, Offer
from sqlalchemy.exc import SQLAlchemyError
import traceback

# Clase que contiene la logica de creción de usuarios
class CreateOffer(BaseCommannd):
    def __init__(self, offer):
        self.validateRequest(offer)

    # Función que valida el request del servicio
    def validateRequest(self, offerJson):
        # Validacion del request
        validateSchema(offerJson, createOfferSchema)
        # Asignacion de variables
        self.postId = offerJson['postId']
        self.description = offerJson['description']
        self.size = offerJson['size']
        self.fragile = offerJson['fragile']
        self.offer = offerJson['offer']

    # Función que realiza creación del usuario
    def execute(self):
        try:
            newOffer = Offer(
                postId=self.postId,
                description=self.description,
                size=self.size,
                fragile=self.fragile,
                offer=self.offer,
            )
            db.session.add(newOffer)
            db.session.commit()
            return newOffer
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
        