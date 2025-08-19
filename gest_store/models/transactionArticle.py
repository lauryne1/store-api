from django.db import models

from gest_store.models.article import Article
from gest_store.models.transaction import Transaction




class TransactionArticle(models.Model):
    """Détails des articles dans une transaction (quantité, prix unitaire)"""
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1, verbose_name="Quantité achetée")
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire au moment de l'achat")
    
    class Meta:
        db_table = 'transaction_articles'
        verbose_name = 'Article de transaction'
        verbose_name_plural = 'Articles de transaction'
        unique_together = ['transaction', 'article']
    
    def __str__(self):
        return f"Transaction #{self.transaction.id} - {self.article.name} x{self.quantite}"
    
    @property
    def sous_total(self):
        return self.quantite * self.prix_unitaire
    