# Generated by Django 4.2.2 on 2023-10-29 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarteiraApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedores',
            name='cod_produto',
        ),
    ]
