# Generated by Django 4.0.1 on 2022-01-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmovidu_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=300)),
                ('requirement', models.CharField(max_length=300)),
                ('ctc', models.CharField(max_length=300)),
                ('compid', models.CharField(max_length=300)),
            ],
        ),
    ]
