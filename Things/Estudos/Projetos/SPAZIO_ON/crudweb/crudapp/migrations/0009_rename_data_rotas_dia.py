# Generated by Django 4.2.2 on 2023-07-29 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0008_remove_abastecimentos_slug_remove_rotas_placa_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rotas',
            old_name='data',
            new_name='dia',
        ),
    ]
