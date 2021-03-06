# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gymcana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('descripcio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('descripcio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProvaCodi',
            fields=[
                ('prova_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Prova')),
            ],
            bases=('app.prova',),
        ),
        migrations.CreateModel(
            name='ProvaTest',
            fields=[
                ('prova_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Prova')),
            ],
            bases=('app.prova',),
        ),
    ]
