from django.urls import path
from . import views

urlpatterns = [
    path('promocoes/', views.promocoes, name='promocoes'),
    path('cardapio/', views.cardapio, name='cardapio'),
]
