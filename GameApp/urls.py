from django.urls import path
from .views import (
    AdicionarJogoView,
    AdicionarDesenvolvedoraView,
    AdicionarReviewView,
    buscar_jogo,
    listar_reviews,
    index,
    registro_view,
    login_view,
    logout_view,
    profile_view,
    editar_profile_view,
    AboutView,
    ReviewDetailView
)

urlpatterns = [
    path('', index, name='index'),
    path('jogo/', AdicionarJogoView.as_view(), name='adicionar_jogo'),
    path('desenvolvedora/', AdicionarDesenvolvedoraView.as_view(), name='adicionar_desenvolvedora'),
    path('review/', AdicionarReviewView.as_view(), name='adicionar_review'),
    path('buscar/', buscar_jogo, name='buscar_jogo'),
    path('reviews/', listar_reviews, name='listar_reviews'),
    path('register/', registro_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('editar-perfil/', editar_profile_view, name='edit_profile'),
    path('about/', AboutView.as_view(), name='about'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),

]
