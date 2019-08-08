from django.urls import path
from .views import Home, About, Ems, Contact

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('contact/', Contact, name='contact-page'),
    path('ems/', Ems, name='ems-page'),

]