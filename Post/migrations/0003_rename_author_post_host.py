# Generated by Django 3.2.9 on 2021-11-04 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20211104_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='host',
        ),
    ]
