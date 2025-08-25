from django.db import models
from django.contrib.auth.models import AbstractUser


class Utilisateur(AbstractUser):
    """Modèle utilisateur pour le système de centre commercial"""
    email = models.EmailField(unique=True)
    negociated_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de négociation/inscription")
    
    # Utiliser email comme identifiant principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'utilisateurs'
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
    
    def __str__(self):
        return f"{self.username} ({self.email})"