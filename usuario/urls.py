from django import views
from .import views
from django.urls import path
#from task.views import login_view, register

app_name = 'task'

urlpatterns = [
    path('', views.login_view, name='login'),
    #path('register/', register, name='register'),  
   # path('inicio', views.inicio, name='index'),
    # Otras rutas y configuraciones de URL
    path('inicio', views.inicio, name='inicio'),
    # Otras rutas y configuraciones de URL
]