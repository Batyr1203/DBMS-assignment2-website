# Generated by Django 4.1.3 on 2022-11-18 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0006_alter_country_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]
