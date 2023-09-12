# Importación de dependencias
from agregators.base_command import BaseCommannd
import traceback
from errors.errors import  InvalidToken, MissingToken, NotFound, InvalidUserPost
from models.models import Origin, Destiny, Route, Offers, Post, Data
import uuid
import os
import requests
import re
import json
from flask import abort, render_template, current_app
import logging


def dict_helper(objlist):
    result2 = [item.obj_to_dict() for item in objlist]
    return result2


def dict_helper(objlist):
    result2 = [item.obj_to_dict() for item in objlist]
    return result2

    
# Función que retorna la información del post
def getPostById( id, headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    # call post/id
    result =  requests.get(POSTS_PATH+'/posts/'+id, headers=headers)
    #post = json.loads(result.json())
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    if result.status_code == 404:
        raise NotFound
    
    return result.json()

# Función que retorna la información del post
def getPostHealth( id, headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    # call post/id
    result =  requests.get(POSTS_PATH+'/posts/ping', headers=headers)
    #post = json.loads(result.json())
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    if result.status_code == 404:
        raise NotFound
    
    return result


# Función que retorna la información del trayecto
def getRouteById( id, headers):
    ROUTES_PATH = os.environ["ROUTES_PATH"]
    # call post/id
    result =  requests.get(ROUTES_PATH+'/routes/'+id, headers=headers)
    #post = json.loads(result.json())
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()


# Función que retorna la oferta del post
def getOffersByPostId( id, headers):
    OFFERS_PATH = os.environ["OFFERS_PATH"]
    params = {'post': id}
    # call Offers/postid
    result =  requests.get(OFFERS_PATH+'/offers',params=params, headers=headers)
    #post = json.loads(result.json())
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()

# Función que retorna la información del score del post
def getScoreByPostId( id, headers):
    SCORES_PATH = os.environ["SCORES_PATH"]    
    # call Offers/postid
    result =  requests.get(SCORES_PATH+'/scores/posts/'+id, headers=headers)
    #post = json.loads(result.json())
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()

def validateToken(headers):
    USERS_PATH = os.environ["USERS_PATH"]
    # call user/me
    result =  requests.get(USERS_PATH+'/users/me', headers=headers)
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()["id"]



#Agregator
def agregator (id, headers):
    ##paso 1 Consultar POST
    current_app.logger.info('Inicia ejecucion de agregator')
    current_app.logger.info('paso 1 obtener información del post por ID')
    responsePost = getPostById(id, headers)    
    
    ### paso 1.1 validar que la publicaicón pertenezca al usuario
    idUser = validateToken(headers)
    
    if idUser != responsePost['userId']:
        traceback.print_exc()
        raise InvalidUserPost
    
     
    ##Pas2 consultar Route asociada al POST
    current_app.logger.info('paso 1 obtener información del trayecto por ID')
    current_app.logger.info('responsePost' + str(responsePost))
    current_app.logger.info('paso 2 obtener información del trayecto post por ID' + responsePost['routeId'])
    responseRoute = getRouteById(responsePost['routeId'], headers)
    
    current_app.logger.info('response route' + str(responseRoute))
    current_app.logger.info('paso 3 obtener información de las ofertas por post  ID' )
   
    responseOffers = getOffersByPostId(id, headers)
    current_app.logger.info('response Offers' + str(responseOffers))
    
    current_app.logger.info('paso 4 obtener el score de un post' )
    responseOffers = getScoreByPostId(id, headers) 
    
    newOrigin = Origin(
        airportCode = responseRoute.get('sourceAirportCode'),
        country = responseRoute.get('sourceAirportCode')
        
    )
    
    newDestiny = Destiny(
        airportCode = responseRoute.get('destinyAirportCode'),
        country = responseRoute.get('destinyCountry')
    )
    
    newRoute = Route(
        id = responseRoute.get('id'),
        flightId = responseRoute.get('flightId'),
        origin = newOrigin.__dict__,
        destiny = newDestiny.__dict__,
        bagcost = responseRoute.get('bagCost')
    )
    
    listOffer = []
    
    for offers in responseOffers:        
        newOffers = Offers(
            id = offers.get('id'),
            userId = offers.get('userId'),
            description = offers.get('userId'),
            size = offers.get('packageSize'),
            fragile = offers.get('isPackageFragile'),
            offer = offers.get('offerAmount'),
            score = float(offers.get('score')),
            createdAt = offers.get('createdAt')
        )
        listOffer.append(newOffers) 
    
    
    newPost = Post(
        id = responsePost.get('id'),
        expireAt = responsePost.get('expireAt') ,
        route = newRoute.__dict__,
        plannedStartDate = responsePost.get('plannedStartDate'),
        plannedEndDate = responsePost.get('plannedEndDate'),
        createdAt = responsePost.get('createdAt'),
        offers = dict_helper(listOffer)
    )
    
    
    newData = Data(
        data = newPost.__dict__
    )
    
    return newData.__dict__
    