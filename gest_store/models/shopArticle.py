from django.db import models
from .article import Article
from .shop import Shop



class ShopArticle(models.Model):
    """Table de liaison entre Shop et Article - Un article peut être dans plusieurs magasins"""
    shop = models.ForeignKey(
        Shop, 
        on_delete=models.CASCADE, 
        related_name='shop_articles',
        verbose_name="Magasin"
    )
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name='shop_articles',
        verbose_name="Article"
    )
    stock = models.IntegerField(default=0, verbose_name="Stock dans ce magasin")
    date_ajout = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout dans le magasin")
    
    class Meta:
        db_table = 'shop_articles'
        verbose_name = 'Article en magasin'
        verbose_name_plural = 'Articles en magasin'
        unique_together = ['shop', 'article']  # Un article ne peut être référencé qu'une fois par magasin
    
    def __str__(self):
        return f"{self.shop.name} - {self.article.name} (Stock: {self.stock})"

