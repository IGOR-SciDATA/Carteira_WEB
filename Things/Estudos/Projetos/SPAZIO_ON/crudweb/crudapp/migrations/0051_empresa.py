# Generated by Django 4.2.2 on 2023-10-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0050_rotas_receber_vlr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('endereco', models.CharField(max_length=60)),
            ],
        ),
    ]
