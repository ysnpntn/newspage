# Generated by Django 4.2.3 on 2023-07-19 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_first_name_post_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='position',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
