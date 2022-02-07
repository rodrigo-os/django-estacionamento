from django.contrib import admin

# Register your models here.

from garagem.models import Tipo, Proprietario, Veiculo, Vaga

admin.site.register(Tipo)
admin.site.register(Proprietario)
admin.site.register(Veiculo)
admin.site.register(Vaga)