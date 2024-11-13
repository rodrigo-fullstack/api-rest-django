from django.db import models

# Create your models here.

# Criando modelagem dos objetos

class Base(models.Model):

    # Criado na data e tempo atual...
    criacao = models.DateTimeField(auto_now_add=True);

    # Data da atualização ...
    atualizacao = models.DateTimeField(auto_now=True);

    # Está ativo?
    ativo = models.BooleanField(default=True);

    # Determina que é classe abstrata
    class Meta:
        abstract = True;

# Classe de Cursos importando a base
class Cursos(Base):
    # Titulo composto de caracteres com no maximo 255
    titulo = models.CharField(max_length=255);

    # Url única do curso 
    url = models.URLField(unique=True);


    class Meta:
        verbose_name = 'Curso';
        verbose_name_plural = 'Cursos';

    # Construtor da classe
    def __str__(self):
        return self.titulo;

# Classe de avaliacoes realizadas
class Avaliacao(Base):

    # Conectando em cursos
    curso = models.ForeignKey(Cursos);

    # Nome com 255 caracteres no máximo
    nome = models.CharField(max_length=255);

    # Campo de email
    email = models.EmailField();

    # Comentário da avaliação do curso, por padrão é vazio
    comentario = models.TextField(blank = True, default='' );

    # Número decimal de 0 a 10
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1);

    class Meta: 
        verbose_name = 'Avaliação';
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}';



