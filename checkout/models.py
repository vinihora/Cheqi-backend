from django.db import models

# Create your models here.
class Teste(models.Model):
    teste = models.CharField(max_length=11)

    def __str__(self):
        return self.teste