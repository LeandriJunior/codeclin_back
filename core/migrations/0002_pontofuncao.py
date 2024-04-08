# Generated by Django 5.0.3 on 2024-03-31 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoFuncao',
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
                ('modulo', models.CharField(max_length=256, null=True)),
            ],
            options={
                'db_table': 'user_pontofuncao',
            },
        ),
    ]
