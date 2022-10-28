from django.db import models
from django.contrib.auth.models import User
class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    resumo = models.TextField()
    texto = models.TextField()
    data = models.DateField()
    data_criacao = models.DateField(auto_now_add=True)
    data_ultima_alteracao = models.DateField(auto_now=True)
    nota = models.FloatField()
    qtd_likes = models.IntegerField()
    status = models.BooleanField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo