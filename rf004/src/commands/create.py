from commands.base_command import BaseCommannd
from errors.errors import ApiError
from validators.validators import validateSchema, createOfferSchema # validatePostId, validatePostExpired, validatePostOwner 
from sqlalchemy.exc import SQLAlchemyError
import requests
import traceback
import json
import os


class CreateOffer(BaseCommannd):
    def __init__(self, postId, post_request_json, headers):
        self.validateRequest(postId, post_request_json, headers)
    
    def validateRequest(self, postId, post_request_json, headers):        
        validateSchema(post_request_json, createOfferSchema)
        # validatePostId(postId, headers)
        # validatePostExpired(postId, headers)
        # validatePostOwner(postId, headers)
        self.headers = headers
        self.postId = postId
        self.description = post_request_json['description']
        self.size = post_request_json['size']
        self.fragile = post_request_json['fragile']
        self.offer = post_request_json['offer']

    def execute(self):
        try:
            data = {"postId": self.postId,
                    "description": self.description,
                    "size": self.size,
                    "fragile": self.fragile,
                    "offer": self.offer
                    }
            OFFERS_PATH = os.environ["OFFERS_PATH"]            
            result = requests.post(f"{OFFERS_PATH}/offers", json=data, headers=self.headers)
            return result            
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)