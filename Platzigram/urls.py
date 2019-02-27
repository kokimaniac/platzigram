
"""Platzigram URL module"""
#Django
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from Platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('helloworld/', local_views.helloworld ),
    path('sortnum/', local_views.sortnum),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)