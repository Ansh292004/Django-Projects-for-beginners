# Generated by Django 5.0.6 on 2024-06-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile_page', '0003_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
