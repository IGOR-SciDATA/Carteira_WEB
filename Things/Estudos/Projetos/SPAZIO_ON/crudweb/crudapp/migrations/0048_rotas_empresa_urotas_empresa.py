# Generated by Django 4.2.2 on 2023-09-11 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0047_notasrecebimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotas',
            name='empresa',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='urotas',
            name='empresa',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]