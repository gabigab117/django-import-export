from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import Magasin, Produit


class ProduitResource(resources.ModelResource):
    magasin = fields.Field(
        column_name='magasin__name',
        attribute='magasin',
        widget=ForeignKeyWidget(Magasin, 'name'))

    class Meta:
        model = Produit
        fields = ('name', 'price', 'stock', 'magasin') # 'magasin__name' is now handled by the widget
        import_id_fields = ('name',) # Unique identifier for import/export
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
