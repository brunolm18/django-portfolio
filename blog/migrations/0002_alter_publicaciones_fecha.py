# Generated by Django 5.0.6 on 2024-06-05 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]