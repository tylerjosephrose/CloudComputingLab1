# Generated by Django 2.1.5 on 2019-03-14 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('temp_max', models.FloatField()),
                ('temp_min', models.FloatField()),
            ],
        ),
    ]
