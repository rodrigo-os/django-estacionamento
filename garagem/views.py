
from django.shortcuts import render
from django.views import generic

# Create your views here.

from garagem.models import Tipo, Proprietario, Veiculo, Vaga


def index(request):
    num_veiculos = Veiculo.objects.all().count()
    num_proprietarios = Proprietario.objects.all().count()
    num_tipos = Tipo.objects.all().count()

    num_vagas_ocupadas = Vaga.objects.filter(situacao__exact='o').count()
    num_vagas_manutencao = Vaga.objects.filter(situacao__exact='m').count()
    num_vagas = Vaga.objects.all().count()


    contexto = {
        'num_veiculos': num_veiculos,
        'num_proprietarios': num_proprietarios,
        'num_tipos': num_tipos,

        'num_vagas_ocupadas': num_vagas_ocupadas,
        'num_vagas_manutencao': num_vagas_manutencao,
        'num_vagas': num_vagas,

    }

    return render(request, 'index.html', context=contexto)


class VehicleListView(generic.ListView):
    model = Veiculo


class VehicleDetailView(generic.DetailView):
    model = Veiculo


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class VehicleCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'garagem.pode_manipular_veiculo'
    model = Veiculo
    fields = '__all__'


class VehicleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'garagem.pode_manipular_veiculo'
    model = Veiculo
    fields = ['modelo', 'fabricante', 'cor', 'tipo']


class VehicleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'garagem.pode_manipular_veiculo'
    model = Veiculo
    success_url = reverse_lazy('veiculos')


class OwnerListView(generic.ListView):
    model = Proprietario


class OwnerDetailView(generic.DetailView):
    model = Proprietario


class OwnerCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'garagem.pode_manipular_proprietario'
    model = Proprietario
    fields = '__all__'


class OwnerUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'garagem.pode_manipular_proprietario'
    model = Proprietario
    fields = '__all__'


class OwnerDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'garagem.pode_manipular_proprietario'
    model = Proprietario
    success_url = reverse_lazy('proprietarios')


class VagaListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'garagem.pode_manipular_vaga'
    model = Vaga

class VagaDetailView(generic.DetailView):
    permission_required = 'garagem.pode_manipular_vaga'
    model = Vaga

class VagaCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'garagem.pode_manipular_vaga'
    model = Vaga
    fields = ['veiculo', 'data_retirada']

class VagaUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'garagem.pode_manipular_vaga'
    model = Vaga
    fields = '__all__'

class VagaDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'garagem.pode_manipular_vaga'
    model = Vaga
    success_url = reverse_lazy('vagas')