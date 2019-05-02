from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=120, unique=True)

class Habilidade(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=200,verbose_name="Descrição/Sobre")

class Pokemon(models.Model):
    imagem = models.FileField(upload_to='fotos/')
    nome = models.CharField(max_length=120)
    altura = models.FloatField()
    fk_categoria = models.ForeignKey('Categoria',on_delete=models.PROTECT)
    fk_habilidades = models.ManyToManyField(Habilidade)
    ponto_saude = models.PositiveIntegerField()
    ataque = models.PositiveIntegerField()
    defesa = models.PositiveIntegerField()
    ataque_especial = models.PositiveIntegerField()
    defesa_especial = models.PositiveIntegerField()
    velocidade = models.PositiveIntegerField()

