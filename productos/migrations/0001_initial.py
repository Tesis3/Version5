# Generated by Django 3.0.3 on 2020-02-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_fin', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(help_text='Descripcion de la Marca', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_fin', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(help_text='Descripcion del Rubro', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Rubros',
            },
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_fin', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(help_text='Descripcion del Segmento', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Segmentos',
            },
        ),
    ]
