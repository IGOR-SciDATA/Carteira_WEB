# Generated by Django 4.2.2 on 2023-10-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0051_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotas',
            name='receber_vlr',
            field=models.FloatField(max_length=6),
        ),
    ]
