# Generated by Django 4.2.6 on 2023-10-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_delete_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
