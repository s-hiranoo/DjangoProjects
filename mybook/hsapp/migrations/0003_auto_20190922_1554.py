# Generated by Django 2.2.4 on 2019-09-22 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0002_auto_20190922_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealerproducts',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='escalation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='farmerinterests',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='prospectfarmer',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]