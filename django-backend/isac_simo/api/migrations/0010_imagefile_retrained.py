# Generated by Django 2.0 on 2020-03-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_imagefile_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefile',
            name='retrained',
            field=models.BooleanField(default=False),
        ),
    ]
