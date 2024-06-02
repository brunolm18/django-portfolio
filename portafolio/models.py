from django.db import models


class Project(models.Model):
    titulo = models.CharField(max_length=100,)
    descripcion = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portafolio/images/')
    url = models.URLField(blank=True)