# Generated by Django 5.0.3 on 2024-04-11 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_grupouser_grupo_remove_grupouser_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
