from django.contrib import admin;
from .models import Avaliacao, Cursos;

# Register your models here.

@admin.register(Cursos)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo');

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'atualizacao', 'ativo');

