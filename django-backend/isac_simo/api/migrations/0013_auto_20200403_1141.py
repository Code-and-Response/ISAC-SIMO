# Generated by Django 2.0 on 2020-04-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200403_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='classifier',
            name='classes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='classifier',
            name='given_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
