from django.shortcuts import render, redirect
from .models import Jogo, Desenvolvedora, Review
from .forms import JogoForm, DesenvolvedoraForm, ReviewForm, BuscaJogoForm
from django.http import HttpResponse

def adicionar_jogo(request):
    form = JogoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('adicionar_jogo')
    return render(request, 'adicionar_jogo.html', {'form': form})

def adicionar_desenvolvedora(request):
    if request.method == 'POST':
        form = DesenvolvedoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DesenvolvedoraForm()

    return render(request, 'adicionar_desenvolvedora.html', {'form': form})

def adicionar_review(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('adicionar_review')
    return render(request, 'adicionar_review.html', {'form': form})

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
    return render(request, 'index.html')

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

