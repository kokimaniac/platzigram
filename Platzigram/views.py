""" Platzigram views."""

#Django modules.
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json
"""Return a greeting"""
def helloworld(request):
    now = datetime.now().strftime('%b %dth, %Y - %H : %M hrs')
    return HttpResponse("<h1 style='color: red;'>Hello World</h1><h2>{now}".format(now=now)+"<h2>")

def sortnum(request):
    """Sort request numbers"""
    numbers = sorted(
        [
            int (i) for i in request.GET["numbers"].split(',')
        ])
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers succesfully sorted!'
    }
    return HttpResponse(json.dumps(data, indent=5), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = '<h1 style="background-color: red;">Sorry {} but you are to child yet</h1>'.format(name)
    else:
        message= '<h1 style="background-color: green;">Hi {} welcome to platzigram!</h1>'.format(name)
    return HttpResponse(message)