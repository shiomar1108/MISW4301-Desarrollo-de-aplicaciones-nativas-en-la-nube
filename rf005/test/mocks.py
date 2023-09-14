from httmock import HTTMock, all_requests, urlmatch
from uuid import uuid4
from datetime import datetime, timedelta


@urlmatch(path=r".*users.*", method="GET")
def mock_post_users_success(url, request):
    return {
        "status_code": 201,
        "content": {
            "id": f"uuid4()",            
            "createdAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z"
        },
    }



@urlmatch(path=r".*/posts.*", method="GET")
def mock_post_rf005_success(url, request):
    return {
        "status_code": 200,
        "content": { },
    }
