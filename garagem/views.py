from django.shortcuts import render
from django.views import generic

# Create your views here.

from garagem.models import Tipo, Proprietario, Veiculo, VagaVeiculo


def index(request):
    num_veiculos = Veiculo.objects.all().count()
    num_vagas = VagaVeiculo.objects.all().count()
    num_tipos = Tipo.objects.all().count()
    num_vagas_ocupadas = VagaVeiculo.objects.filter(situacao__exact='o').count()
    num_vagas_manutencao = VagaVeiculo.objects.filter(situacao__exact='m').count()
    num_proprietarios = Proprietario.objects.all().count()

    contexto = {
        'num_veiculos': num_veiculos,
        'num_vagas': num_vagas,
        'num_tipos': num_tipos,
        'num_vagas_ocupadas': num_vagas_ocupadas,
        'num_vagas_manutencao': num_vagas_manutencao,
        'num_proprietarios': num_proprietarios
    }

    return render(request, 'index.html', context=contexto)


class VehicleListView(generic.ListView):
    model = Veiculo
