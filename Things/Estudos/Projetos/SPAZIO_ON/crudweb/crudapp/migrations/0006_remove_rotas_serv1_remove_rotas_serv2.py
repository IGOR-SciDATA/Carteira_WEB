# Generated by Django 4.2.2 on 2023-07-25 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_alter_rotas_serv2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rotas',
            name='serv1',
        ),
        migrations.RemoveField(
            model_name='rotas',
            name='serv2',
        ),
    ]