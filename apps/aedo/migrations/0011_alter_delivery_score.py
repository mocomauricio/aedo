# Generated by Django 3.2.7 on 2021-09-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aedo', '0010_auto_20210912_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(0, '----'), (1, 'MALO'), (2, 'REGULAR'), (3, 'BUENO'), (4, 'MUY BUENO'), (5, 'EXCELENTE')], default=0, verbose_name='valoracion del cliente'),
        ),
    ]
