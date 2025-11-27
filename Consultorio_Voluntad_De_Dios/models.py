from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nombre