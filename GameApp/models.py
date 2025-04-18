from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils import timezone

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.PositiveIntegerField()
    descricao = models.TextField()
    genero = models.CharField(max_length=100)
    desenvolvedora = models.ForeignKey('Desenvolvedora', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.ano_lancamento})"


class Review(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    comentario = models.TextField()
    nota = models.IntegerField()  # <-- Esse campo é essencial!
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jogo.titulo} - {self.autor}"
    
# class Post(models.Model):
#     titulo = models.CharField(max_length=100)
#     subtitulo = models.CharField(max_length=150)
#     corpo = RichTextField()
#     imagem = models.ImageField(upload_to='posts/', blank=True, null=True)
#     criado_em = models.DateTimeField(auto_now_add=True)
#     autor = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.titulo

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='avatares', null=True, blank=True)


    def __str__(self):
        return f"{self.user.username} - {self.imagem}"

class Mensagem(models.Model):
    remetente = models.ForeignKey(User, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensagens_recebidas', on_delete=models.CASCADE)
    assunto = models.CharField(max_length=100)
    corpo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False) 

    def __str__(self):
        return f"De {self.remetente} para {self.destinatario}: {self.assunto}"

@receiver(post_save, sender=User)
def criar_perfil_automaticamente(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

