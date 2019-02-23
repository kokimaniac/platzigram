
"""Platzigram URL module"""

from django.urls import path
from Platzigram import views


urlpatterns = [
    path('helloworld/', views.helloworld ),
    path('sortnum/', views.sortnum),
    path('hi/<str:name>/<int:age>/', views.say_hi),
]
