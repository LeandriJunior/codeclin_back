# Generated by Django 5.0.3 on 2024-04-11 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('cliente', '0002_rename_usuario_user_user'),
        ('funcionario', '0003_alter_funcionario_user'),
        ('user', '0012_remove_userlogin_usuario_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserLogin',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]