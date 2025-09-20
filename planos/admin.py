from django.contrib import admin
from .models import Plano, Vantagem

@admin.register(Vantagem)
class VantagemAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_inicial', 'preco_recorrente')
    filter_horizontal = ('vantagens',)
