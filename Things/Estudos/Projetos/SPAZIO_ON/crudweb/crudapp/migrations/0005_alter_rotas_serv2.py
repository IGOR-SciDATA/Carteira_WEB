# Generated by Django 4.2.2 on 2023-07-25 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_alter_rotas_serv1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotas',
            name='serv2',
            field=models.CharField(max_length=60),
        ),
    ]
