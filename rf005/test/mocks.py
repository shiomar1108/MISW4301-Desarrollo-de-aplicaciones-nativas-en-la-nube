from httmock import HTTMock, all_requests, urlmatch
from uuid import uuid4
from datetime import datetime, timedelta




@urlmatch(path=r".*/rf005/posts.*", method="GET")
def mock_post_rf005_success(url, request):
    return {
        "status_code": 201,
        "content": {  
            
             "data": {
                "createdAt": "2023-09-12T03:02:22.247160",
                "expireAt": "2023-09-19T03:02:22.207000",
                "id": "7db2089e-51e7-11ee-a25b-0242ac120005",
                "offers": [
                    {
                    "createdAt": "2023-09-12T03:03:42.024589",
                    "description": "c2f4a7d1-267c-42ee-a990-349171aa5a12",
                    "fragile": true,
                    "id": "14490464-5585-46bc-bf48-a872dfb7729b",
                    "offer": "45.64",
                    "score": 42.9,
                    "size": "SMALL",
                    "userId": "ddb14b0f-bba1-41af-bace-a59b310483a5"
                },
                {
                    "createdAt": "2023-09-12T03:03:18.421256",
                    "description": "c2f4a7d1-267c-42ee-a990-349171aa5a12",
                    "fragile": false,
                    "id": "1c3be390-d57c-4c2c-9183-fca18b47f53b",
                    "offer": "43.31",
                    "score": 29.57,
                    "size": "LARGE",
                    "userId": "ddb14b0f-bba1-41af-bace-a59b310483a5"
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
                "id": "a66afbbc-7347-4e8d-b849-95f35a584ce3",
                "origin": {
                    "airportCode": "BOG",
                    "country": "BOG"
                }
            }
        }
          
        },
    }
