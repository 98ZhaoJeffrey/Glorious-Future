# Generated by Django 3.1.4 on 2020-12-04 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('token', models.UUIDField(blank=True)),
                ('organizationName', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('token', models.UUIDField(blank=True)),
                ('firstName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('school', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
