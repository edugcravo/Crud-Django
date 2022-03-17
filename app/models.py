from django.db import models

# Create your models here.
class Livros(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    descricao = models.CharField(max_length=200)
    isbn = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.description