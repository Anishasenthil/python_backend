# Generated by Django 4.1.12 on 2023-11-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcreation', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
