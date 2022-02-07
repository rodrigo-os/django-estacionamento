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

urlpatterns += [
    path('proprietarios/', views.OwnerListView.as_view(), name='proprietarios'),
    path('proprietarios/<int:pk>', views.OwnerDetailView.as_view(), name='proprietario-detalhes'),
    path('proprietario/create/', views.OwnerCreate.as_view(), name='proprietario-create'),
    path('proprietario/<int:pk>/update/', views.OwnerUpdate.as_view(), name='proprietario-update'),
    path('proprietario/<int:pk>/delete/', views.OwnerDelete.as_view(), name='proprietario-delete'),
]

urlpatterns += [
    path('vagas/', views.VagaListView.as_view(), name='vagas'),
    path('vagas/<int:pk>', views.VagaDetailView.as_view(), name='vaga-detalhes'),
    path('vaga/', views.VagaCreate.as_view(), name='vaga-create'),
    path('vaga/<int:pk>/update/', views.VagaUpdate.as_view(), name='vaga-update'),
    path('vaga/<int:pk>/delete/', views.VagaDelete.as_view(), name='vaga-delete'),
]
