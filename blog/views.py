from django.shortcuts import render, get_object_or_404
from .models import Publicaciones

def publicaciones(request):
    publicaciones = Publicaciones.objects.all()
    return render(request,"publicaciones.html",{"publicaciones":publicaciones})

def publicacion_detail(request,publicacion_id):
    publicacion = get_object_or_404(Publicaciones,pk=publicacion_id)
    return render(request,"publicacion_detail.html",{"publicacion":publicacion})