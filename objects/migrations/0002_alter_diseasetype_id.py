# Generated by Django 4.1.2 on 2022-11-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasetype',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
