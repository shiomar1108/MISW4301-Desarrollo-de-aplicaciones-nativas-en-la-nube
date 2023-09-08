from datetime import datetime

class Origin():
    airportCode : str
    country : str
    
    def __init__(self, airportCode, country):
        self.airportCode = airportCode
        self.country = country
    
class Destiny():
    airportCode : str
    country : str
    
    def __init__(self, airportCode, country):
        self.airportCode = airportCode
        self.country = country
    
    
class Route():
    id : str
    flightId : str
    origin : Origin
    destiny: Destiny
    bagcost: int
    
    def __init__(self,id, flightId, origin,destiny,bagcost):
        self.id = id
        self.flightId = flightId
        self.origin = origin
        self.destiny = destiny
        self.bagcost = bagcost
    
    
class Offers():
    id : str
    userId : str
    description : str
    size : str
    fragile : str
    offer : str
    score : str
    createdAt : datetime
    
    def __init__(self,id, userId, description,size,fragile,offer,score,createdAt):
        self.id = id
        self.userId = userId
        self.description = description
        self.size = size
        self.fragile = fragile
        self.offer = offer
        self.score = score
        self.createdAt = createdAt
    
    
class Post():
    id : str
    expireAt : datetime
    route : Route
    plannedStartDate : datetime
    plannedEndDate : datetime
    createdAt : datetime
    offers : Offers


    def __init__(self, id, expireAt, route, plannedStartDate, plannedEndDate, createdAt, offers ):
        self.id = id
        self.expireAt = expireAt
        self.route = route
        self.plannedStartDate =  plannedStartDate
        self.plannedEndDate = plannedEndDate
        self.createdAt = createdAt
        self.offers = offers
        