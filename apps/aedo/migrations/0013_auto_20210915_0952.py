# Generated by Django 3.2.7 on 2021-09-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aedo', '0012_auto_20210914_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='received',
            field=models.IntegerField(default=0, verbose_name='cobrado por Gestor'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='received2',
            field=models.IntegerField(default=0, verbose_name='cobrado por AEDO'),
        ),
    ]
