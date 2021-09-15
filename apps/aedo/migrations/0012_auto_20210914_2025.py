# Generated by Django 3.2.7 on 2021-09-15 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aedo', '0011_alter_delivery_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='received2',
            field=models.IntegerField(default=0, verbose_name='cobrado por el AEDO'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='deliver_date',
            field=models.DateField(null=True, verbose_name='fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='deliver_time',
            field=models.TimeField(null=True, verbose_name='hora de entrega'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='received',
            field=models.IntegerField(default=0, verbose_name='cobrado por el Gestor'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='reception_date',
            field=models.DateField(null=True, verbose_name='fecha de retiro'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='reception_time',
            field=models.TimeField(null=True, verbose_name='hora de retiro'),
        ),
    ]
