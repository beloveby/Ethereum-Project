# Generated by Django 2.1.7 on 2019-04-17 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pools',
            new_name='Pool',
        ),
    ]