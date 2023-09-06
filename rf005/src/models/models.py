from datetime import datetime

class Post(db.Model):
    id : str
    routeId : str
    userId : str
    createdAt : DateTime
    expireAt : DateTime


    def __init__(self, id, routeId, userId, createdAt, expireAt):
        self.id = id
        self.routeId = routeId
        self.userId = userId
        self.createdAt =  createdAt
        self.expireAt = expireAt