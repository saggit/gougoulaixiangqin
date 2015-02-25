from datetime import datetime
from django.http import HttpResponse
import json

def json_response_result(func):
    def wraps(request, *args, **kwargs):
        begin_time = datetime.now()
        result = func(request, *args, **kwargs)
        end_time = datetime.now()
        result["total_time"] = (end_time - begin_time).total_seconds()
        return HttpResponse(json.dumps(result))
    return wraps
