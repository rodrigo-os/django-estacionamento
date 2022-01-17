from django.urls import path
from garagem import views

urlpatterns = [
    path('', views.index, name='index'),
    path('veiculos/', views.VehicleListView.as_view(), name='veiculos')
]
