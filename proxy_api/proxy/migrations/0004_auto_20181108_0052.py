# Generated by Django 2.1 on 2018-11-08 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0003_auto_20181108_0042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apicalllog',
            old_name='body',
            new_name='content',
        ),
    ]