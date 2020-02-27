from django.urls import path

from . import views

urlpatterns = [
    path('room/', views.rooms, name='r'),
    path('sess/', views.sess, name='s'),
    path('speaker/',views.speakers, name='s'),
    path('', views.homePage, name='s'),
]