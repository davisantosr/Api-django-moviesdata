# Generated by Django 3.1.3 on 2020-11-03 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedata',
            old_name='nome',
            new_name='name',
        ),
    ]
