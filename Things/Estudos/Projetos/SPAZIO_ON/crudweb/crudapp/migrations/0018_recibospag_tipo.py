# Generated by Django 4.2.2 on 2023-07-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0017_alter_abastecimentos_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibospag',
            name='tipo',
            field=models.CharField(default='a', max_length=60),
        ),
    ]
