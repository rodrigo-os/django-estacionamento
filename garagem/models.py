from django.db import models
from django.urls import reverse

# Create your models here.

class Tipo(models.Model):
    nome = models.CharField(max_length=100, help_text='Entre com o tipo do veículo. Ex: Automóvel.')

    def __str__(self):
        return self.nome


class Proprietario(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['primeiro_nome','ultimo_nome']
        permissions = (("pode_manipular_proprietario", "Manipula o cadastro de proprietários."),)

    def get_absolute_url(self):
        return reverse('proprietario-detalhes', args=[str(self.id)])

    def __str__(self):
        return f'{self.primeiro_nome} {self.ultimo_nome}'


class Veiculo(models.Model):
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    cor = models.CharField(max_length=20, help_text='Entre com a cor predominante do veículo. Ex: Prata')
    proprietario = models.ForeignKey(Proprietario, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['modelo']
        permissions = (("pode_manipular_veiculo", "Manipula o cadastro de veículos."),)

    def get_absolute_url(self):
        return reverse('veiculo-detalhes', args=[str(self.id)])

    def __str__(self):
        return f'{self.fabricante}/{self.modelo}'


from datetime import date

class Vaga(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)
    data_retirada = models.DateField(null=True, blank=True)

    SITUACAO_VAGA = (
        ('o', 'Ocupada'),
        ('m', 'Manutenção'),
    )

    situacao = models.CharField(
        max_length=1,
        choices=SITUACAO_VAGA,
        blank=True,
        default='o',
        help_text='Situação da vaga',
    )

    def esta_atrasado(self):
        if self.data_retirada and date.today() > self.data_retirada:
            return True
        return False

    class Meta:
        ordering = ['data_retirada']
        permissions = (("pode_manipular_vaga", "Manipula o cadastro de vagas."),)

    def get_absolute_url(self):
        return reverse('vaga-detalhes', args=[str(self.id)])

    def __str__(self):
        return f'{self.id} ({self.veiculo})'


