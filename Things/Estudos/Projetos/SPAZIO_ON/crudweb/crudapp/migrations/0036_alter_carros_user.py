# Generated by Django 4.2.2 on 2023-08-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0035_carros_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='user',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
