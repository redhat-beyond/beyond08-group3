# Generated by Django 4.1.3 on 2023-01-05 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_client_client_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_account',
            new_name='cclient_account',
        ),
    ]