# Generated by Django 4.2.2 on 2023-10-29 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarteiraApp', '0005_alter_vendas_cod_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='cod_promo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='codpromo', to='CarteiraApp.promocoes'),
        ),
    ]
