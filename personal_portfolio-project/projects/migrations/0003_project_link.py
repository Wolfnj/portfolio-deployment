# Generated by Django 3.0.1 on 2019-12-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20191218_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default=''),
        ),
    ]