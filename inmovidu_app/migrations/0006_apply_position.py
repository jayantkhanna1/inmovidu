# Generated by Django 4.0.1 on 2022-01-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmovidu_app', '0005_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='position',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
