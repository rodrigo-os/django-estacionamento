from django.db import models


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
        ordering = ['ultimo_nome', 'primeiro_nome']

    def __str__(self):
        return f'{self.primeiro_nome} {self.ultimo_nome}'


class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.SET_NULL, null=True)
    fabricante = models.TextField(max_length=100)
    cor = models.CharField(max_length=20, help_text='Entre com a cor predominante do veículo. Ex: Prata')
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.fabricante}/{self.modelo}'


import uuid


class VagaVeiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Identificador único em todo o estacionamento, referente a vaga e ao veículo que a ocupa.')
    data_retirada = models.DateField(null=True, blank=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)

    SITUACAO_VAGA = (
        ('o', 'Ocupada'),
        ('d', 'Disponível'),
        ('r', 'Reservada'),
        ('m', 'Manutenção'),
    )

    situacao = models.CharField(
        max_length=1,
        choices=SITUACAO_VAGA,
        blank=True,
        default='o',
        help_text='Situação da vaga',
    )

    class Meta:
        ordering = ['data_retirada']

    def __str__(self):
        return f'{self.id} ({self.veiculo.modelo})'
