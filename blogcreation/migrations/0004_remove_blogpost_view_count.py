# Generated by Django 4.1.12 on 2023-11-14 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogcreation', '0003_blogpost_view_count_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='view_count',
        ),
    ]
