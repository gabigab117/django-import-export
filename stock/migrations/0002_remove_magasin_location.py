# Generated by Django 5.2.1 on 2025-06-03 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magasin',
            name='location',
        ),
    ]
