# Generated by Django 4.2.2 on 2023-08-23 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0031_remove_rotas_serv1_remove_rotas_serv2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recibospag',
            old_name='id_rota',
            new_name='desc_pag',
        ),
        migrations.RemoveField(
            model_name='recibospag',
            name='desc',
        ),
    ]
