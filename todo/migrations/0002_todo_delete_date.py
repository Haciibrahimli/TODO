# Generated by Django 4.2.6 on 2023-10-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='delete_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
