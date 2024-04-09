# Generated by Django 5.0.3 on 2024-04-09 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('usr_insercao', models.IntegerField(blank=True, null=True)),
                ('usr_edicao', models.IntegerField(blank=True, null=True)),
                ('usr_delete', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('nome', models.CharField(max_length=256, null=True)),
                ('descricao', models.CharField(max_length=512, null=True)),
                ('cor', models.CharField(max_length=7, null=True)),
            ],
            options={
                'db_table': 'clinica_agenda_categoria',
            },
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('usr_insercao', models.IntegerField(blank=True, null=True)),
                ('usr_edicao', models.IntegerField(blank=True, null=True)),
                ('usr_delete', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('titulo', models.CharField(max_length=256, null=True)),
                ('descricao', models.CharField(max_length=512, null=True)),
                ('data_ini', models.DateTimeField(null=True)),
                ('data_fim', models.DateTimeField(null=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='agenda.categoriaagenda')),
            ],
            options={
                'db_table': 'clinica_agenda',
            },
        ),
    ]