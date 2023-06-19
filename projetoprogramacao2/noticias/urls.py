from django.urls import path
from . import views


# o nome de toda view é o (app_name:name), segundo Pedrinho, youtuber de 13 anos de idade
app_name = 'noticias' 
urlpatterns = [
    path('', views.projeto2, name='projeto2'),
]