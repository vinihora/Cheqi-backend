# Generated by Django 4.0.6 on 2023-06-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
