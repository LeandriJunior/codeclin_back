# Generated by Django 5.0.3 on 2024-04-11 01:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_pontofuncao'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('usr_insercao', models.IntegerField(blank=True, null=True)),
                ('usr_edicao', models.IntegerField(blank=True, null=True)),
                ('usr_delete', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('celular_numero', models.CharField(max_length=50, null=True)),
                ('celular_ddd', models.CharField(max_length=3, null=True)),
                ('celular_completo', models.CharField(max_length=50, null=True)),
                ('celular_completo_form', models.CharField(max_length=50, null=True)),
                ('telefone_numero', models.CharField(max_length=50, null=True)),
                ('telefone_ddd', models.CharField(max_length=3, null=True)),
                ('telefone_completo', models.CharField(max_length=50, null=True)),
                ('telefone_completo_form', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('email_financeiro', models.EmailField(max_length=200, null=True)),
                ('email_documentacao', models.EmailField(max_length=200, null=True)),
                ('nm_completo', models.CharField(max_length=200, null=True)),
                ('nm_primeiro', models.CharField(max_length=200, null=True)),
                ('nm_ultimo', models.CharField(max_length=200, null=True)),
                ('nm_social_completo', models.CharField(max_length=200, null=True)),
                ('nm_social_primeiro', models.CharField(max_length=200, null=True)),
                ('nm_social_ultimo', models.CharField(max_length=200, null=True)),
                ('nm_documento_completo', models.CharField(max_length=200, null=True)),
                ('nm_documento_primeiro', models.CharField(max_length=200, null=True)),
                ('nm_documento_ultimo', models.CharField(max_length=200, null=True)),
                ('cpf', models.BigIntegerField(null=True)),
                ('cpf_form', models.CharField(max_length=20, null=True)),
                ('rg', models.CharField(max_length=15, null=True)),
                ('rg_form', models.CharField(max_length=15, null=True)),
                ('passaporte', models.CharField(max_length=200, null=True)),
                ('passaporte_form', models.CharField(max_length=200, null=True)),
                ('dat_nasc', models.DateField(null=True)),
                ('imagem', models.TextField(default='fotos/sem-foto.png', null=True)),
                ('nm_mae', models.CharField(max_length=200, null=True)),
                ('nm_pai', models.CharField(max_length=200, null=True)),
                ('is_cliente', models.BooleanField(default=False)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='endereco', to='core.endereco')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]