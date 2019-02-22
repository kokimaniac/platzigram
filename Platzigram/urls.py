
from django.http import HttpResponse
from django.urls import path

def helloworld(request):
    return HttpResponse("<h1 style='color: red;'>Hello World</h1>")


urlpatterns = [
    path('helloworld/', helloworld),
]
