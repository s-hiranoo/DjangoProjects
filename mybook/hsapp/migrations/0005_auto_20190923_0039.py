# Generated by Django 2.2.4 on 2019-09-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0004_auto_20190923_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='state_id_picture',
            field=models.FilePathField(blank=True, default=''),
        ),
    ]
