from django.db import models

class Arroz(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome