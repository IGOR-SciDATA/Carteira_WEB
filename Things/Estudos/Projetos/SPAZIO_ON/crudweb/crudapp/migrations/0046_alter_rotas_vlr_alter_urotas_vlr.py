# Generated by Django 4.2.2 on 2023-09-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0045_alter_abastecimentos_vlr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotas',
            name='vlr',
            field=models.FloatField(max_length=6),
        ),
        migrations.AlterField(
            model_name='urotas',
            name='vlr',
            field=models.FloatField(max_length=6),
        ),
    ]
