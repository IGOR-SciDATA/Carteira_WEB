# Generated by Django 4.2.2 on 2023-08-23 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0032_rename_id_rota_recibospag_desc_pag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibospag',
            name='desc_pag',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
