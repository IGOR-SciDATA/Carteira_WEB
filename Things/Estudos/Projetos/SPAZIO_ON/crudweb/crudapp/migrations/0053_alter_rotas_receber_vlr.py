# Generated by Django 4.2.2 on 2023-10-07 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0052_alter_rotas_receber_vlr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotas',
            name='receber_vlr',
            field=models.FloatField(default=None, max_length=6),
        ),
    ]