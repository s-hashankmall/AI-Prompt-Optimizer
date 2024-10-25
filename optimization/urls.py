from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('optimize/', views.get_answer, name='get_answer'),  
    path('save_ratings/', views.save_ratings, name='save_ratings'),  
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'), 
]
