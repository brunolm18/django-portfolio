from django.db import models
import datetime 


class Publicaciones(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="blog/images")
    fecha = models.DateField(default=datetime.date.today)
    
