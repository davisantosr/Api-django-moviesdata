# Generated by Django 3.1.3 on 2020-11-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201103_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='action', max_length=100),
        ),
    ]
