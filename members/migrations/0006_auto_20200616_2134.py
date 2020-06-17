# Generated by Django 3.0.6 on 2020-06-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_member_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='rovers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='rov')),
                ('year', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='quote',
            field=models.CharField(max_length=100),
        ),
    ]
