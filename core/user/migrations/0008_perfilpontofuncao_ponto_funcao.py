# Generated by Django 5.0.3 on 2024-04-03 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_pontofuncao'),
        ('user', '0007_remove_perfilpontofuncao_ponto_funcao'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilpontofuncao',
            name='ponto_funcao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.pontofuncao'),
        ),
    ]
