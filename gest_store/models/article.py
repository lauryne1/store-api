from django.db import models
from .categorie import Categorie


class Article(models.Model):
    """Modèle pour les articles"""
    name = models.CharField(max_length=100, verbose_name="Nom de l'article")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    stock = models.IntegerField(default=0, verbose_name="Stock disponible")
    opened_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ouverture/création")
    category = models.ForeignKey(
        Categorie, 
        on_delete=models.CASCADE,  # Un article appartient obligatoirement à une catégorie
        related_name='articles',
        verbose_name="Catégorie"
    )
    
    class Meta:
        db_table = 'articles'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.price}€ (Cat: {self.category.name})"