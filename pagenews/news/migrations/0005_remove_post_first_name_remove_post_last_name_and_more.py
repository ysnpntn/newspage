# Generated by Django 4.2.3 on 2023-07-19 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='position',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
