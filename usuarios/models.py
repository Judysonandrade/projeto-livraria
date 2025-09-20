from django.contrib.auth.models import AbstractUser
from django.db import models
from planos.models import Plano

class Usuario(AbstractUser):
    plano = models.ForeignKey(
        Plano,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Plano do Usuário"
    )

    # Evita conflito com auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_user_set',  # <- altera aqui
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_user_permissions_set',  # <- altera aqui
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
