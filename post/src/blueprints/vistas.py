from flask_restful import Resource
from flask import request, jsonify
from commands import create, delete, get, query, reset
from models.model import PostSchema
from validators.validators import validateToken


publicacion_schema = PostSchema()

class VistaPosts(Resource):

    def post(self):
        validateToken(request.headers)
        try:
            newPostObj = create.CreatePost(post_request_json=request.get_json())
        except Exception as e:
            if e.__class__.__name__=='InvalidExpirationDate':
                return jsonify({"msg": "La fecha de expiración no es válida"})
        else:
            new_post = newPostObj.execute()
            return jsonify({"id":new_post.id, "userId":new_post.userId, "createdAt":new_post.createdAt.replace(microsecond=0).isoformat()}), 201        

    def get(self):
        validateToken(request.headers)
        PostQueryObj = query.QueryPost(post_request_args=request.args)        
        return [publicacion_schema.dump(post) for post in PostQueryObj.execute()]


class VistaPostsReset(Resource):

    def delete(self):        
        PostResetObj = reset.ResetPosts()
        PostResetObj.execute()        
        return jsonify({"msg": "Todos los datos fueron eliminados"})


class VistaPost(Resource):

    def get(self, postId):
        validateToken(request.headers)
        PostGetObj = get.GetPost(postId=postId)
        return publicacion_schema.dump(PostGetObj.execute())

    def delete(self, postId):
        validateToken(request.headers)
        PostDeleteObj = delete.DeletePost(postId=postId)
        PostDeleteObj.execute()        
        return jsonify({"msg": "la publicación fue eliminada"})        
       

class VistaPostHealthCheck(Resource):
    def get(self):
        return jsonify({'status': 'pong'})