from django.db import models

# Create your models here.
class Encuesta(models.Model):
    nombre = models.CharField(max_length=50)  
    email = models.EmailField()               
    contraseña = models.CharField(max_length=50)
    comentario = models.TextField()
    torneo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
