# Generated by Django 4.0.6 on 2023-06-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0003_remove_profile_id_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doc',
            field=models.CharField(default='', max_length=14, unique=True),
        ),
    ]
