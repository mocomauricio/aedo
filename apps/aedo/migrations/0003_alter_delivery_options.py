# Generated by Django 3.2.7 on 2021-09-02 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aedo', '0002_delivery_package'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'permissions': (('read', 'Puede ver la lista'),), 'verbose_name': 'Entrega', 'verbose_name_plural': 'Entregas'},
        ),
    ]
