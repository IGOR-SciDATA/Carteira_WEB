# Generated by Django 4.2.2 on 2023-07-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0019_alter_recibospag_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibospag',
            name='moto',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]