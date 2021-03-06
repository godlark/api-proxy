# Generated by Django 2.0.9 on 2018-11-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('format', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='api',
            name='accepted_content_types',
            field=models.ManyToManyField(to='proxy.ContentType'),
        ),
        migrations.AddField(
            model_name='api',
            name='methods',
            field=models.ManyToManyField(to='proxy.Method'),
        ),
    ]
