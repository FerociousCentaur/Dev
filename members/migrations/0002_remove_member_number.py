# Generated by Django 3.0.6 on 2020-06-15 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='number',
        ),
    ]
