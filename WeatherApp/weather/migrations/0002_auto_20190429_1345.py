# Generated by Django 2.2 on 2019-04-29 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='names',
            new_name='name',
        ),
    ]