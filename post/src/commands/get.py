from commands.base_command import BaseCommannd
from errors.errors import ApiError, PostDoNotExist
from validators.validators import validateUUID
from models.model import Post
from sqlalchemy.exc import SQLAlchemyError
import traceback


class GetPost(BaseCommannd):
    def __init__(self, postId):
        self.postId = postId        

    def execute(self):
        try:
            validateUUID(self.postId)
            post = Post.query.filter(Post.id == self.postId).first()
            if post is None:
                raise PostDoNotExist   
            return post
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)