# Generated by Django 4.2.3 on 2023-07-19 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
