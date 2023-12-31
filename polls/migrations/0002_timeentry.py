# Generated by Django 4.2.7 on 2023-11-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='datetime started')),
                ('end_time', models.DateTimeField(verbose_name='datetime ended')),
                ('notes', models.CharField(max_length=10000)),
            ],
        ),
    ]
