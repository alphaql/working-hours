# Generated by Django 2.2.1 on 2019-06-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working_hours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workinghour',
            name='festive',
            field=models.BooleanField(default=False),
        ),
    ]
