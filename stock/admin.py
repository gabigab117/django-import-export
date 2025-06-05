from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import Magasin, Produit


class ProduitResource(resources.ModelResource):
    magasin = fields.Field(
        column_name='magasin__name', # Nom de la colonne dans le fichier d'import/export
        attribute='magasin', # Attribut du modèle Produit
        widget=ForeignKeyWidget(Magasin, 'name')) # Widget pour gérer la relation ForeignKey

    class Meta:
        model = Produit
        fields = ('name', 'price', 'stock', 'magasin') # 'magasin__name' is now handled by the widget
        import_id_fields = ('name',) # Vérifie si le nom du produit existe déjà pour éviter les doublons
        # Si il y a deux éléments dans le tuples, un produit est considéré comme existant si les deux éléments sont identiques
        skip_unchanged = True  # Ignore les lignes qui ne modifient pas les données existantes lors de l'importation
        report_skipped = True  # Inclut les lignes ignorées dans le rapport d'importation


@admin.register(Magasin)
class MagasinAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Produit)
class ProduitAdmin(ImportExportModelAdmin):
    resource_class = ProduitResource
    list_display = ['name', 'price', 'stock', 'magasin']
    search_fields = ['name']
    list_filter = ['magasin']
