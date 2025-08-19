from django.db import models


class Shop(models.Model):
    """Modèle pour les magasins du centre commercial"""
    name = models.CharField(max_length=100, verbose_name="Nom du magasin")
    location = models.CharField(max_length=200, verbose_name="Localisation dans le centre")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        db_table = 'shops'
        verbose_name = 'Magasin'
        verbose_name_plural = 'Magasins'
    
    def __str__(self):
        return f"{self.name} - {self.location}"