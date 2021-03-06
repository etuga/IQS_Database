# Generated by Django 3.0.7 on 2020-06-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('smiles', models.CharField(max_length=200)),
                ('author_name', models.CharField(choices=[('ENDIKA', 'Endika'), ('RAI', 'Rai')], default='Endika', max_length=10)),
                ('project_name', models.CharField(choices=[('PANCREAS', 'PanTCK'), ('ZAP', 'ZAP')], max_length=10)),
            ],
        ),
    ]
