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

# Clase que cotiene la definición del modelo de base de datos de Usuario
class Offer(db.Model):
    __tablename__ = "offers"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    postId = db.Column(db.String(64), unique=True)
    userId = db.Column(db.String(64))
    description = db.Column(db.String(140))
    size = db.Column(db.String(140), default="SMALL")
    fragile = db.Column(db.Boolean,default=True)
    offer = db.Column(db.Float, precision=2)
    createdAt = db.Column(DateTime, default=datetime.utcnow)


# Clase que autogenera el esquema del modelo Usuario
class OfferSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Offer
        id = fields.String() 