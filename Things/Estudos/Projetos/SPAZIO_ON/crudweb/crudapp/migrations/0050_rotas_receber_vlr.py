# Generated by Django 4.2.2 on 2023-09-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0049_alter_carros_options_alter_perfil_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotas',
            name='receber_vlr',
            field=models.FloatField(default=None, max_length=6),
        ),
    ]
