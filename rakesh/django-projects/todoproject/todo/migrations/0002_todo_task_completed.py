# Generated by Django 3.2.8 on 2021-11-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='task_completed',
            field=models.BooleanField(default=False),
        ),
    ]
