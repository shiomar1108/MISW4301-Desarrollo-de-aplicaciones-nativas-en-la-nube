from httmock import HTTMock, all_requests, urlmatch
from uuid import uuid4
from datetime import datetime, timedelta


@urlmatch(path=r".*routes.*", method="POST")
def mock_post_route_success(url, request):
    return {
        "status_code": 201,
        "content": {
            "id": f"uuid4()",
            "flightId": "889",
            "sourceAirportCode": "BOG",
            "sourceCountry": "Colombia",
            "destinyAirportCode": "MDE",
            "destinyCountry": "Mexico",
            "bagCost": 123,
            "plannedStartDate": f"{str(datetime.today() + timedelta(days=1)).split('.')[0].replace(' ', 'T')}.214Z",
            "plannedEndDate": f"{str(datetime.today() + timedelta(days=10)).split('.')[0].replace(' ', 'T')}.214Z",
            "createdAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z",
        },
    }


@urlmatch(path=r".*post.*", method="POST")
def mock_post_posts_success(url, request):
    return {
        "status_code": 201,
        "content": {
            "id": f"uuid4()",
            "routeId":  f"uuid4()",
            "userId": "BOG",
            "createdAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z",
            "expireAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z"            
        },
    }


@urlmatch(path=r".*users.*", method="POST")
def mock_post_users_success(url, request):
    return {
        "status_code": 201,
        "content": {
            "id": f"uuid4()",            
            "createdAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z"
        },
    }



@urlmatch(path=r".*offers.*", method="POST")
def mock_post_offers_success(url, request):
    return {
        "status_code": 201,
        "content": {               
            "createdAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z",
            "id": f"uuid4()",
            "userId": f"uuid4()"
        },
    }



@urlmatch(path=r".*scores.*", method="POST")
def mock_post_scores_success(url, request):
    return {
        "status_code": 201,
        "content": {               
            "createdAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z",
            "id": f"uuid4()",
            "isPackageFragile": False,
            "offerAmount":"43.36",
            "offerId":f"uuid4()",
            "packageAmount":"21.28",
            "packageDescription": "consequatur corrupti eos",
            "packageSize": "SMALL",
            "postId":f"uuid4()",
            "score":"38.45",
            "userId": f"uuid4()"
        },
    }
