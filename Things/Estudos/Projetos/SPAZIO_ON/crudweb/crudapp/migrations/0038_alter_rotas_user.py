# Generated by Django 4.2.2 on 2023-08-28 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crudapp', '0037_remove_urotas_carro_alter_urotas_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotas',
            name='user',
            field=models.ForeignKey(default='a', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
