# Generated by Django 5.0.3 on 2024-04-15 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_rename_descricao_agenda_observacao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='paciente',
            new_name='cliente',
        ),
    ]