# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError
from commands.update import UpdateUser
from models.models import UserSchema
from validators.validators import validateSchema, verifyCallbackSchema
import logging
import os

# Constantes
SCORE_VALIDATE =  os.getenv("SCORE_VALIDATE", default="80")
LOG = "[Verify User]"

# Esquemas 
userSchema = UserSchema()

# Clase que contiene la logica de verificación de usuarios
class VerifyUser(BaseCommannd):
    def __init__(self, data):
        validateSchema(data, verifyCallbackSchema)
        self.data = data
  
    # Función que valida el status de un usuario
    def validateStatusUser(self, score):
        userStatus = "NO_VERIFICADO"
        if int(score) >= int(SCORE_VALIDATE):
            userStatus = "VERIFICADO"
        return userStatus
    
    # Función que realiza la actualización del usuario
    def execute(self):
        try:
            logging.info(f"{LOG} Transaction request => ")
            logging.info(self.data)
            dataToUpdate = {"status": f"{self.validateStatusUser(self.data['score'])}"}
            logging.info(f"{LOG} User status from TrueNative => ")
            logging.info(dataToUpdate)
            userUpdated = UpdateUser(self.data['userIdentifier'], dataToUpdate).execute()
            userUpdatedJson = userSchema.dump(userUpdated)
            logging.info(f"{LOG} Transaction response => ")
            logging.info(userUpdatedJson)
            return userUpdatedJson
        except Exception as e:
            logging.error(e)
            raise ApiError(e)
