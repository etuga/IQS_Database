# Generated by Django 3.0.7 on 2020-06-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(choices=[('ENDIKA', 'Endika')], default='name', max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('tag', models.CharField(choices=[('DOCKING', 'Docking'), ('MD', 'Molecular Dynamics')], default='tag', max_length=100)),
                ('script', models.CharField(max_length=500)),
            ],
        ),
    ]