# usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):

    model = Usuario
    
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'plano')
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'plano')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('plano',)}),  # Adiciona campo plano
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('plano',)}),  # Adiciona campo plano
    )
    
      # Adiciona campo plano


admin.site.register(Usuario, UsuarioAdmin)

