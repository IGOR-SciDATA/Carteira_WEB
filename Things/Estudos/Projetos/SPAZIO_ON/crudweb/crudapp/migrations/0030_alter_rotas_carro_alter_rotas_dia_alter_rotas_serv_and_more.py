# Generated by Django 4.2.2 on 2023-08-14 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crudapp', '0029_alter_rotas_carro_alter_rotas_dia_alter_rotas_serv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotas',
            name='carro',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='rotas',
            name='dia',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='rotas',
            name='serv',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='rotas',
            name='user',
            field=models.ForeignKey(default='a', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rotas',
            name='vlr',
            field=models.CharField(max_length=6),
        ),
    ]
