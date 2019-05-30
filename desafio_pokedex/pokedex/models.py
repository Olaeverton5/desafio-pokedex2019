from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.nome

    def __int__(self):
        return self.id


class Habilidade(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=200,verbose_name="Descrição/Sobre")

    def __str__(self):
        return self.nome

class EstiloCard(models.Model):
    descricao = models.CharField(max_length=20, unique=True)
    classe = models.CharField(max_length=40, unique=True)
    def __str__(self):
        return self.descricao

class Pokemon(models.Model):
    imagem = models.FileField(upload_to='fotos/')
    nome = models.CharField(max_length=120)
    altura = models.FloatField()
    fk_categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    fk_habilidades = models.ManyToManyField(Habilidade)
    ponto_saude = models.PositiveIntegerField()
    ataque = models.PositiveIntegerField()
    defesa = models.PositiveIntegerField()
    ataque_especial = models.PositiveIntegerField()
    defesa_especial = models.PositiveIntegerField()
    velocidade = models.PositiveIntegerField()
    estilo_card = models.ForeignKey('EstiloCard', on_delete=models.PROTECT, verbose_name="Estilo CSS do card", null=True, blank=True)

    def __str__(self):
        return self.nome
