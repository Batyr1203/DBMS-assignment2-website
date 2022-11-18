# Generated by Django 4.1.3 on 2022-11-18 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0008_discover_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('salary', models.PositiveIntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.country')),
            ],
        ),
    ]
