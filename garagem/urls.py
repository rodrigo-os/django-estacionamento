from django.urls import path
from garagem import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('veiculos/', views.VehicleListView.as_view(), name='veiculos'),
    path('veiculos/<int:pk>', views.VehicleDetailView.as_view(), name='veiculo-detalhes'),
    path('veiculo/create/', views.VehicleCreate.as_view(), name='veiculo-create'),
    path('veiculo/<int:pk>/update/', views.VehicleUpdate.as_view(), name='veiculo-update'),
    path('veiculo/<int:pk>/delete/', views.VehicleDelete.as_view(), name='veiculo-delete'),
]
