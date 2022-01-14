from django.urls import path
from garagem import views

urlpatterns = [
    path('', views.index, name='index')
]
