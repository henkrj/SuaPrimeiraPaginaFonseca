from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, DetailView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.contrib.auth.models import User

from .models import Jogo, Desenvolvedora, Review, Profile, Mensagem
from .forms import JogoForm, DesenvolvedoraForm, ReviewForm, BuscaJogoForm, RegistroForm, ProfileForm, MensagemForm

class AdicionarJogoView(LoginRequiredMixin, CreateView):
    model = Jogo
    form_class = JogoForm
    template_name = 'adicionar_jogo.html'
    success_url = reverse_lazy('adicionar_jogo')

    def form_valid(self, form):
        titulo = form.cleaned_data.get('titulo')
        ano_lancamento = form.cleaned_data.get('ano_lancamento')

        if Jogo.objects.filter(titulo__iexact=titulo, ano_lancamento=ano_lancamento).exists():
            form.add_error('titulo', 'Já existe um jogo com este título e ano de lançamento.')
            return self.form_invalid(form)

        return super().form_valid(form)

#Versão antiga
# def adicionar_jogo(request):
    # form = JogoForm(request.POST or None)
    # if form.is_valid():
        # form.save()
        # return redirect('adicionar_jogo')
    # return render(request, 'adicionar_jogo.html', {'form': form})


class AdicionarDesenvolvedoraView(LoginRequiredMixin, CreateView):
    model = Desenvolvedora
    form_class = DesenvolvedoraForm
    template_name = 'adicionar_desenvolvedora.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        nome = form.cleaned_data.get('nome')
        if Desenvolvedora.objects.filter(nome__iexact=nome).exists():
            form.add_error('nome', 'Esta desenvolvedora já está cadastrada.')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['desenvolvedoras'] = Desenvolvedora.objects.all().order_by('nome')
        return context


    
# def adicionar_desenvolvedora(request):
    # if request.method == 'POST':
        # form = DesenvolvedoraForm(request.POST)
        # if form.is_valid():
            # form.save()
            # return redirect('index')
    # else:
        # form = DesenvolvedoraForm()

    # return render(request, 'adicionar_desenvolvedora.html', {'form': form})

class AdicionarReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'adicionar_review.html'
    success_url = reverse_lazy('adicionar_review')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
# def adicionar_review(request):
    # form = ReviewForm(request.POST or None)
    # if form.is_valid():
        # form.save()
        # return redirect('adicionar_review')
    # return render(request, 'adicionar_review.html', {'form': form})
class EditarReviewView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'editar_review.html'
    success_url = reverse_lazy('listar_reviews')

    def test_func(self):
        review = self.get_object()
        return self.request.user.username == review.autor

class ExcluirReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'excluir_review.html'
    success_url = reverse_lazy('listar_reviews')

    def test_func(self):
        review = self.get_object()
        return self.request.user.username == review.autor

class ReviewUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'editar_review.html'
    success_url = reverse_lazy('listar_reviews')
    success_message = "Review atualizada com sucesso!"

    def get_queryset(self):
        # Apenas o autor pode editar a própria review
        return Review.objects.filter(autor=self.request.user)

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'excluir_review.html'
    success_url = reverse_lazy('listar_reviews')

    def get_queryset(self):
        # Apenas o autor pode excluir a própria review
        return Review.objects.filter(autor=self.request.user)

def buscar_jogo(request):
    resultados = None
    form = BuscaJogoForm(request.GET or None)
    if form.is_valid():
        termo = form.cleaned_data['termo']
        resultados = Jogo.objects.filter(titulo__icontains=termo)
    return render(request, 'buscar_jogo.html', {'form': form, 'resultados': resultados})


def listar_reviews(request):
    reviews = Review.objects.select_related('jogo').order_by('-id')
    return render(request, 'listar_reviews.html', {'reviews': reviews})


def index(request):
    total_jogos = Jogo.objects.count()
    total_desenvolvedoras = Desenvolvedora.objects.count()
    total_reviews = Review.objects.count()
    ultimos_jogos = Jogo.objects.order_by('-id')[:5]

    context = {
        'total_jogos': total_jogos,
        'total_desenvolvedoras': total_desenvolvedoras,
        'total_reviews': total_reviews,
        'ultimos_jogos': ultimos_jogos,
    }
    return render(request, 'index.html', context)


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistroForm()
    return render(request, 'GameApp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'GameApp/login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'GameApp/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def profile_view(request):
    return render(request, 'GameApp/profile.html')


@login_required
def editar_profile_view(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'GameApp/edit_profile.html', {'form': form})



class AboutView(TemplateView):
    template_name = "about.html"
    
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'
    context_object_name = 'review'
    
class CaixaEntradaView(LoginRequiredMixin, ListView):
    model = Mensagem
    template_name = 'mensagens/caixa_entrada.html'
    context_object_name = 'mensagens'

    def get_queryset(self):
        return Mensagem.objects.filter(destinatario=self.request.user).order_by('-data_envio')

class EnviarMensagemView(LoginRequiredMixin, CreateView):
    model = Mensagem
    form_class = MensagemForm
    template_name = 'GameApp/enviar_mensagem.html'
    success_url = reverse_lazy('caixa_entrada')

    def form_valid(self, form):
        form.instance.remetente = self.request.user
        if form.instance.destinatario == self.request.user:
            form.add_error('destinatario', 'Você não pode enviar uma mensagem para si mesmo.')
            return self.form_invalid(form)
        return super().form_valid(form)

class MensagemDetailView(LoginRequiredMixin, DetailView):
    model = Mensagem
    template_name = 'mensagens/detalhe_mensagem.html'
    context_object_name = 'mensagem'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.destinatario != self.request.user:
            raise PermissionDenied("Você não tem permissão para visualizar esta mensagem.")

        if not obj.lida:
            obj.lida = True
            obj.save()

        return obj

class ResponderMensagemView(LoginRequiredMixin, CreateView):
    model = Mensagem
    form_class = MensagemForm
    template_name = 'mensagens/responder_mensagem.html'
    success_url = reverse_lazy('caixa_entrada')

    def get_initial(self):
        destinatario = get_object_or_404(User, pk=self.kwargs['pk'])
        return {
            'destinatario': destinatario,
            'assunto': f"Re: ",
        }

    def form_valid(self, form):
        form.instance.remetente = self.request.user
        return super().form_valid(form)
    
class CaixaSaidaView(LoginRequiredMixin, ListView):
    model = Mensagem
    template_name = 'mensagens/caixa_saida.html'
    context_object_name = 'mensagens'

    def get_queryset(self):
        return Mensagem.objects.filter(remetente=self.request.user).order_by('-data_envio')
    
class MensagemEnviadaDetailView(LoginRequiredMixin, DetailView):
    model = Mensagem
    template_name = 'mensagens/mensagem_enviada_detail.html'
    context_object_name = 'mensagem'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.remetente != self.request.user:
            raise PermissionDenied("Você não tem permissão para visualizar esta mensagem.")
        return obj
