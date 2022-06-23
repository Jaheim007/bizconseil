from django.urls import path
from .views import index, about, error, testimonial, feature, quote, team, contact, service

urlpatterns = [
    path('', index , name='index'),
    path('about', about , name='about'),
    path('404', error , name='error'),
    path('testimonial', testimonial , name='testimonial'),
    path('feature', feature , name='feature'),
    path('quote', quote , name='quote'),
    path('team', team , name='team'), 
    path('contact', contact, name='contact'),
    path('service', service, name='service'),
   
]