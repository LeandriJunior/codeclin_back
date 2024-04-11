# Generated by Django 5.0.3 on 2024-04-11 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('usr_insercao', models.IntegerField(blank=True, null=True)),
                ('usr_edicao', models.IntegerField(blank=True, null=True)),
                ('usr_delete', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('codigo', models.IntegerField(null=True)),
                ('nome', models.CharField(max_length=200, null=True)),
                ('tipo', models.CharField(max_length=200, null=True)),
                ('cnpj', models.CharField(max_length=200, null=True)),
                ('inscricao_estadual', models.CharField(max_length=200, null=True)),
                ('cnes', models.CharField(max_length=200, null=True)),
                ('razao_social', models.CharField(max_length=200, null=True)),
                ('nome_fantasia', models.CharField(max_length=200, null=True)),
                ('data_abertura', models.DateField(null=True)),
                ('data_fechamento', models.DateField(null=True)),
                ('telefone', models.CharField(max_length=200, null=True)),
                ('celular', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'filial',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('usr_insercao', models.IntegerField(blank=True, null=True)),
                ('usr_edicao', models.IntegerField(blank=True, null=True)),
                ('usr_delete', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('nome', models.CharField(max_length=200, null=True)),
                ('tipo', models.CharField(max_length=200, null=True)),
                ('area_pai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_area', to='filial.area')),
            ],
            options={
                'db_table': 'filial_area',
            },
        ),
    ]
