# Generated by Django 3.0.7 on 2020-06-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_auto_20200615_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='script',
            name='body',
        ),
        migrations.AddField(
            model_name='script',
            name='code',
            field=models.TextField(default='Script Code Goes Here'),
        ),
    ]
