from django.urls import path
from .views import publicaciones,publicacion_detail
app_name = "blog"

urlpatterns = [
    path("",publicaciones,name="publicaciones"),
    path("<int:publicacion_id>",publicacion_detail,name="publicacion_detail"),
]