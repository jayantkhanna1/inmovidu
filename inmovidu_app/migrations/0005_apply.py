# Generated by Django 4.0.1 on 2022-01-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmovidu_app', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('yop', models.CharField(max_length=300)),
                ('resume', models.CharField(max_length=300)),
                ('jobid', models.CharField(max_length=300)),
            ],
        ),
    ]
