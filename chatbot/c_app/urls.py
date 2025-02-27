from django.urls import path
from .views import *

urlpatterns = [
    path('', chatbot_ui, name='chatbot_ui'),
    path('ask/', ask_question, name='ask_question'),
    
]
