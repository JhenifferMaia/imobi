from django.urls import include
from django.urls import path
from django.urls import path
from . import views
# a função path  permite que a gente crie uma nova url
# Se tiver dado essa mensagem por causa de versão do 'pip ',  após instalar o pip install django ->  WARNING: You are using pip version...
#Digite o comando --> python -m pip install --upgrade pip
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name="sair")
    
]

#pip install django
#pip install pillow
#venv/Scripts/Activate
#reinstalar os pip e ativar o ambiente virtual, caso o servidor dê problema. E usar o comando: python -m pip install --upgrade pip