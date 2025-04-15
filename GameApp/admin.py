from django.contrib import admin
from .models import Desenvolvedora, Jogo, Review

@admin.register(Desenvolvedora)
class DesenvolvedoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais')
    search_fields = ('nome',)

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'ano_lancamento', 'desenvolvedora')
    list_filter = ('genero', 'ano_lancamento')
    search_fields = ('titulo',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('jogo', 'autor', 'nota', 'data_criacao')
    list_filter = ('nota', 'data_criacao')
    search_fields = ('jogo__titulo', 'autor', 'comentario')

