# Generated by Django 4.2.2 on 2023-09-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0040_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibospag',
            name='desc_pag',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]