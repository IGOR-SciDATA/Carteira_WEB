# Generated by Django 4.2.2 on 2023-07-29 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0010_alter_abastecimentos_carro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abastecimentos',
            old_name='data',
            new_name='dia',
        ),
        migrations.RenameField(
            model_name='recibospag',
            old_name='data',
            new_name='dia',
        ),
    ]
