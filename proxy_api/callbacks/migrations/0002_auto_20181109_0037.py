# Generated by Django 2.1 on 2018-11-09 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callbacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callbackcalllog',
            old_name='api',
            new_name='callback',
        ),
    ]
