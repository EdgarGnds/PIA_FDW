from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('cartas/', views.cartas, name='cartas'),
    path('clanes/', views.clanes, name='clanes'),
    path('esports/', views.esports, name='esports'),
    path('mazos/', views.mazos, name='mazos'),
    path('encuesta/', views.encuesta_view, name='encuesta'),
]