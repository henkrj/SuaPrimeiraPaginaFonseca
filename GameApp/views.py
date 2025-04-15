from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,TemplateView,DetailView
from django.urls import reverse_lazy

from .models import Jogo, Desenvolvedora, Review, Profile
from .forms import JogoForm, DesenvolvedoraForm, ReviewForm, BuscaJogoForm, RegistroForm, ProfileForm

class AdicionarJogoView(LoginRequiredMixin, CreateView):
    model = Jogo
    form_class = JogoForm
    template_name = 'adicionar_jogo.html'
    success_url = reverse_lazy('adicionar_jogo')

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
    profile = request.user.profile
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