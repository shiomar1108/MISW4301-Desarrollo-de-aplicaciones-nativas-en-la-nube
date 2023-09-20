# Importación de dependencias
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

# Creación de variable db
db = SQLAlchemy()

# Clase que cotiene la definición del modelo de base de datos
class TarjetaCredito(db.Model):
    __tablename__ = "tarjetaCredito"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    token = db.Column(db.String(256), nullable=False)
    userId = db.Column(UUID(as_uuid=True), nullable=False)
    lastFourDigits = db.Column(db.String(4), nullable=False)
    ruv = db.Column(db.String(64), nullable=False)  # Pendiente corroborar longitud de cadena de caracteres
    issuer = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updateAt = db.Column(DateTime, nullable=True)
    
class TarjetaCreditoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TarjetaCredito
        id = fields.String() 