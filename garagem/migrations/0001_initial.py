# Generated by Django 4.0 on 2022-01-12 22:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=100)),
                ('ultimo_nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['ultimo_nome', 'primeiro_nome'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Entre com o tipo do veículo. Ex: Automóvel.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('fabricante', models.TextField(max_length=100)),
                ('cor', models.CharField(help_text='Entre com a cor predominante do veículo. Ex: Prata', max_length=20)),
                ('proprietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garagem.proprietario')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garagem.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='VagaVeiculo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador único em todo o estacionamento, referente a vaga e ao veículo que a ocupa.', primary_key=True, serialize=False)),
                ('data_retirada', models.DateField(blank=True, null=True)),
                ('situacao', models.CharField(blank=True, choices=[('o', 'Ocupada'), ('d', 'Disponível'), ('r', 'Reservada'), ('m', 'Manutenção')], default='o', help_text='Situação da vaga', max_length=1)),
                ('veiculo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garagem.veiculo')),
            ],
            options={
                'ordering': ['data_retirada'],
            },
        ),
    ]
