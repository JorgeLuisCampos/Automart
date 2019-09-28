from django.db import models

# Create your models here.
class Auto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    modelo = models.DecimalField(max_digits=4, decimal_places=0)
    img_url = models.TextField()

    def __str__(self):
        return self.nombre