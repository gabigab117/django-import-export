<!-- filepath: /Users/gabrieltrouve/Pro/mentorats/imex/README.md -->

# Import / Export dans l'application Stock

Ce projet Django utilise **django-import-export** dans l'administration pour importer et exporter les produits et magasins.

## Points clés (d'après ton code)

- **Resource personnalisée (`ProduitResource`)** :
  - Déclare un champ `magasin` avec `ForeignKeyWidget` pour résoudre la relation par `name`.
  - `fields` : spécifie quelles colonnes seront disponibles à l'import/export.
  - `import_id_fields` : définit le champ unique (`name`) pour identifier les enregistrements existants lors de l'import.
  - Active `skip_unchanged` et `report_skipped` pour ignorer et signaler les lignes sans changement.

- **Admin (`ImportExportModelAdmin`)** :
  - Enregistre `Magasin` et `Produit` via les classes `MagasinAdmin` et `ProduitAdmin`.
  - Affiche et filtre les données (`list_display`, `search_fields`, `list_filter`).

## Installation et configuration

1. Ajouter dans `requirements.txt` :
   ```text
   django-import-export
   openpyxl
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Dans `settings.py`, ajouter à `INSTALLED_APPS` :
   ```python
   INSTALLED_APPS = [
       # ...
       'import_export',
       'stock',
   ]
   ```

## Utilisation

- **Import** : via l’interface admin, bouton “Import” sur le modèle `Produit`.
- **Export** : bouton “Export” pour récupérer les données au format CSV ou Excel (`.xlsx`).

---

