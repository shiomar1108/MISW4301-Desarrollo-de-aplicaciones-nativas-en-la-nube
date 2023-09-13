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




@urlmatch(path=r".*/rf005/posts/.*", method="POST")
def mock_post_scores_success(url, request):
    return {
        "status_code": 201,
        "content": {  
            
             "data": {
                "createdAt": "2023-09-12T03:02:22.247160",
                "expireAt": "2023-09-19T03:02:22.207000",
                "id": "cb08a884-5118-11ee-b571-0242ac190005",
                "offers": [
                    {
                    "createdAt": "2023-09-12T03:03:42.024589",
                    "description": "c2f4a7d1-267c-42ee-a990-349171aa5a12",
                    "fragile": true,
                    "id": "14490464-5585-46bc-bf48-a872dfb7729b",
                    "offer": "45.64",
                    "score": 42.9,
                    "size": "SMALL",
                    "userId": "c2f4a7d1-267c-42ee-a990-349171aa5a12"
                },
                {
                    "createdAt": "2023-09-12T03:03:18.421256",
                    "description": "c2f4a7d1-267c-42ee-a990-349171aa5a12",
                    "fragile": false,
                    "id": "1c3be390-d57c-4c2c-9183-fca18b47f53b",
                    "offer": "43.31",
                    "score": 29.57,
                    "size": "LARGE",
                    "userId": "c2f4a7d1-267c-42ee-a990-349171aa5a12"
                }
            ],
            "plannedEndDate": null,
            "plannedStartDate": null,
            "route": {
                "bagcost": 728,
                "destiny": {
                    "airportCode": "LGW",
                    "country": "Inglaterra"
                },
                "flightId": "634",
                "id": "cc9700ec-dbb1-4316-82f0-c35551c79481",
                "origin": {
                    "airportCode": "BOG",
                    "country": "BOG"
                }
            }
        }
          
        },
    }
