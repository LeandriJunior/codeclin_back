# Generated by Django 5.0.3 on 2024-04-11 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usuario',
            new_name='user',
        ),
    ]
