# Generated by Django 3.0.5 on 2020-05-11 15:15

import crawler.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20200424_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='extra_data',
            field=crawler.models.JSONField(null=True),
        ),
    ]
