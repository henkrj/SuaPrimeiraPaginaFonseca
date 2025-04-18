from django import forms
from .models import Jogo, Desenvolvedora, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Mensagem

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['titulo', 'ano_lancamento', 'descricao', 'genero', 'desenvolvedora']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        ano_lancamento = cleaned_data.get('ano_lancamento')

        if Jogo.objects.filter(titulo__iexact=titulo, ano_lancamento=ano_lancamento).exists():
            raise forms.ValidationError("Este jogo já foi cadastrado com esse ano.")
        return cleaned_data
    
#versão1
# class JogoForm(forms.ModelForm):
#     class Meta:
#         model = Jogo
#         fields = '__all__'

class DesenvolvedoraForm(forms.ModelForm):
    class Meta:
        model = Desenvolvedora
        fields = ['nome']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if Desenvolvedora.objects.filter(nome__iexact=nome).exists():
            raise forms.ValidationError("Essa desenvolvedora já está cadastrada.")
        return nome
 
#versão1    
# class DesenvolvedoraForm(forms.ModelForm):
#     class Meta:
#         model = Desenvolvedora
#         fields = ['nome']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['jogo', 'nota', 'comentario']

class BuscaJogoForm(forms.Form):
    termo = forms.CharField(label='Buscar por título')
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    nascimento = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'nascimento']

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['destinatario', 'assunto', 'corpo']