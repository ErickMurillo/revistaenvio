# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 17:35
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0004_auto_20160915_0644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autores',
            options={'ordering': ('nombre',), 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='revistas',
            options={'ordering': ('-numero',), 'verbose_name': 'Revista', 'verbose_name_plural': 'Revistas'},
        ),
        migrations.AlterModelOptions(
            name='temas',
            options={'ordering': ('tema',), 'verbose_name': 'Tema', 'verbose_name_plural': 'Temas'},
        ),
        migrations.AlterModelOptions(
            name='zonas',
            options={'ordering': ('zona',), 'verbose_name': 'Zona', 'verbose_name_plural': 'Zonas'},
        ),
        migrations.AddField(
            model_name='articulos',
            name='opinion',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='autornota',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Introducci\xf3n'),
        ),
        migrations.AlterField(
            model_name='autores',
            name='cargo',
            field=models.TextField(blank=True, null=True, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='autores',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='autores',
            name='nombre',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='autores',
            name='nombre_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre ingles'),
        ),
        migrations.AlterField(
            model_name='autores',
            name='nombre_es',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre en espa\xf1ol'),
        ),
        migrations.AlterField(
            model_name='autores',
            name='nota',
            field=models.TextField(blank=True, null=True, verbose_name='Nota'),
        ),
        migrations.AlterField(
            model_name='autores',
            name='titulo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Titulo'),
        ),
    ]
