from django.db import models


class Categorie(models.Model):
    """Modèle pour les catégories d'articles"""
    name = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
    description = models.TextField(blank=True, verbose_name="Description")
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
    
    def __str__(self):
        return self.name