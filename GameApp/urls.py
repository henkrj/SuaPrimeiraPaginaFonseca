from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
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
    AboutView,ReviewDetailView,
    EditarReviewView,ExcluirReviewView,
    CaixaEntradaView,EnviarMensagemView,
    MensagemDetailView,ResponderMensagemView,
    CaixaSaidaView,MensagemEnviadaDetailView,
    
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
    path('review/<int:pk>/editar/', EditarReviewView.as_view(), name='editar_review'),
    path('review/<int:pk>/excluir/', ExcluirReviewView.as_view(), name='excluir_review'),
    path('mensagens/', CaixaEntradaView.as_view(), name='caixa_entrada'),
    path('mensagens/nova/', EnviarMensagemView.as_view(), name='enviar_mensagem'),
    path('mensagens/<int:pk>/', MensagemDetailView.as_view(), name='mensagem_detail'),
    path('mensagens/responder/<int:pk>/', ResponderMensagemView.as_view(), name='responder_mensagem'),
    path('mensagens/enviadas/', CaixaSaidaView.as_view(), name='caixa_saida'),
    path('mensagens/enviadas/<int:pk>/', MensagemEnviadaDetailView.as_view(), name='mensagem_enviada_detail'),
      path('alterar-senha/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),

    path('senha-alterada/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'
    ), name='password_change_done'),


]
