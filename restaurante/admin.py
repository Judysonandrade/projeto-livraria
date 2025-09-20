from django.contrib import admin
from .models import PromocaoEvento, CardapioItem, Funcionario, FeedbackCliente

admin.site.register(PromocaoEvento)
admin.site.register(CardapioItem)
admin.site.register(Funcionario)
admin.site.register(FeedbackCliente)