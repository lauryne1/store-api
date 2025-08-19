# models.py
from django.db import models
from .article import Article
from .shop import Shop
from .utilisateur import Utilisateur



class Transaction(models.Model):
    """Modèle pour les transactions - Plusieurs transactions par utilisateur, chaque transaction liée à un magasin"""
    client = models.ForeignKey(
        Utilisateur, 
        on_delete=models.CASCADE, 
        related_name='transactions',
        verbose_name="Client"
    )
    shop = models.ForeignKey(
        Shop, 
        on_delete=models.CASCADE, 
        related_name='transactions',
        verbose_name="Magasin"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant total")
    transaction_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de transaction")
    
    # Articles achetés dans cette transaction (Many-to-Many avec quantités)
    articles = models.ManyToManyField(
        Article,
        through='TransactionArticle',
        related_name='transactions'
    )
    
    class Meta:
        db_table = 'transactions'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ['-transaction_date']
    
    def __str__(self):
        return f"Transaction #{self.id} - {self.client.username} - {self.amount}€ - {self.shop.name}"