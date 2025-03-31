from django import forms
from .models import Jogo, Desenvolvedora, Review

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'


class DesenvolvedoraForm(forms.ModelForm):
    class Meta:
        model = Desenvolvedora
        fields = ['nome']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class BuscaJogoForm(forms.Form):
    termo = forms.CharField(label='Buscar por título')