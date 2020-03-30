from django.contrib import admin
from .models import Usuario
from .models import Departamento
from .models import Automovel
from .models import Solicitar
from .models import AtenderSolicitacao

# Register your models here.
@admin.register(Usuario, Departamento, Automovel,Solicitar, AtenderSolicitacao)
class UsuarioAdmin(admin.ModelAdmin):
	pass
class DepartamentoAdmin(admin.ModelAdmin):
	pass
class AutomovelAdmin(admin.ModelAdmin):
	pass
class SolicitarAdmin(admin.ModelAdmin):
	pass
class AtenderSolicitacaoAdmin(admin.ModelAdmin):
	pass