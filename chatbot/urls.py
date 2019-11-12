from django.urls import path
from chatbot import views

app_name='chatbot'
urlpatterns=[
	path('text',views.chat_bot,name='chat_bot'),
]