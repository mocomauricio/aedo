# Generated by Django 3.2.7 on 2021-09-12 08:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aedo', '0008_report_userreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='fecha'),
        ),
        migrations.AlterField(
            model_name='userreport',
            name='base_amount',
            field=models.IntegerField(default=0, verbose_name='base'),
        ),
    ]