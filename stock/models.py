from django.db import models


class Magasin(models.Model):
    """
    Represents a store or warehouse where products are stored.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Magasin"
        verbose_name_plural = "Magasins"
        ordering = ['name']


class Produit(models.Model):
    """
    Represents a product that can be stored in a Magasin.
    """
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    magasin = models.ForeignKey(Magasin, related_name='produits', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['name']
