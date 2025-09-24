from django.urls import path
from . import views

urlpatterns = [
    path('promocoes/', views.promocoes, name='promocoes'),
    path('executivo/', views.executivo, name='executivo'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('', views.equipe, name='equipe'),
    path('historia/', views.feedbacks, name='feedbacks'),
    path('reservar/', views.criar_reserva, name='criar_reserva'),
    path('faleconosco/', views.fale_conosco, name='fale_conosco'),
    path('especialidades/', views.especialidades, name='especialidades'),
]
