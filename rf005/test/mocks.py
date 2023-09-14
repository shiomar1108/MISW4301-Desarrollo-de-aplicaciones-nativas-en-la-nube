from httmock import HTTMock, all_requests, urlmatch
from uuid import uuid4
from datetime import datetime, timedelta


@urlmatch(path=r".*users/me.*", method="GET")
def mock_post_users_success(url, request):
    return {
        "status_code": 201,
        "content": {
            "dni":"573",
            "email":"edwina72@hotmail.com",
            "fullName":"kelly kuvalis phd",
            "id":"ddb14b0f-bba1-41af-bace-a59b310483a5",
            "phoneNumber":"4484535552",
            "status":"NO_VERIFICADO",
            "username":"ray"
        },
    }



@urlmatch(path=r".*/posts.*", method="GET")
def mock_post_rf005_success(url, request):
    return {
        "status_code": 201,
        "content": {
            "id": "7db2089e-51e7-11ee-a25b-0242ac120005",
            "routeId": "a66afbbc-7347-4e8d-b849-95f35a584ce3",
            "userId": "ddb14b0f-bba1-41af-bace-a59b310483a5",
            "createdAt": "2023-09-13T03:41:58.317925",
            "expireAt": "2023-09-20T03:41:58.272000"
            },
    }
