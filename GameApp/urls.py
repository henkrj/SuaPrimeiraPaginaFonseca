from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('desenvolvedora/', views.adicionar_desenvolvedora, name='adicionar_desenvolvedora'),
    path('jogo/', views.adicionar_jogo, name='adicionar_jogo'),
    path('review/', views.adicionar_review, name='adicionar_review'),
    path('buscar/', views.buscar_jogo, name='buscar_jogo'),
    path('reviews/', views.listar_reviews, name='listar_reviews'),

]
