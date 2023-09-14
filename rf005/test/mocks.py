from httmock import HTTMock, all_requests, urlmatch
from uuid import uuid4
from datetime import datetime, timedelta




@urlmatch(path=r".*/rf005/posts.*", method="GET")
def mock_post_rf005_success(url, request):
    return {
        "status_code": 200,
        "content": { },
    }
