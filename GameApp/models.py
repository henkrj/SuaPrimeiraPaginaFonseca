from django.db import models

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_lancamento = models.IntegerField()
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Review(models.Model):
    jogo = models.ForeignKey('Jogo', on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    comentario = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)  # <-- Aqui

    def __str__(self):
        return f"{self.jogo.titulo} - {self.autor} ({self.nota})"