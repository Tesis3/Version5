# Generated by Django 3.0.3 on 2020-02-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='fecha_fin',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='rubro',
            name='fecha_fin',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='segmento',
            name='fecha_fin',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
