# Generated by Django 3.0.3 on 2020-02-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0002_auto_20200226_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='fecha_fin',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
