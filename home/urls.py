
from django.urls import path
from .views import *


urlpatterns = [
   path('', home, name='home') ,
   path('api/get_quiz', get_quiz, name='get_quiz') 
]

