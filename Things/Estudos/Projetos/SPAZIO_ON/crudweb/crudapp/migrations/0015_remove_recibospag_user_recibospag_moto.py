# Generated by Django 4.2.2 on 2023-07-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0014_alter_recibospag_id_rota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recibospag',
            name='user',
        ),
        migrations.AddField(
            model_name='recibospag',
            name='moto',
            field=models.CharField(default='A', max_length=60),
        ),
    ]
