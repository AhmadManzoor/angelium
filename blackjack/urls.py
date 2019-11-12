from django.urls import path
from . import views

app_name='blackjack'
urlpatterns=[
	path('',views.index,name='index'),
	path('<int:id>/',views.details,name='details'),
	path('<int:id>/choice/', views.choice, name='choice'),
]