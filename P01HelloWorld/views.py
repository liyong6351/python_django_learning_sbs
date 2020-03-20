from django.http import HttpResponse
import json


def index(request):
    resp = {
        'code': '200',
        'message': 'success',
        'data': {
            'num': '1234',
        },
    }

    return HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8',
                            status='200',
                            reason='success',
                            charset='utf-8')
