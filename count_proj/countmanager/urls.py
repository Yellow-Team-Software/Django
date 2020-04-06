from django.urls import path

from . import views

urlpatterns = [

    path('', views.homePage, name='s'),
    path('bme/<str:pk>/', views.bme, name='bme'),
    path('count/<str:pk>/<str:bme>/', views.recordCount, name='record_count')
]