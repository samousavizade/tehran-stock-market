# Generated by Django 3.0.5 on 2020-05-18 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0004_auto_20200518_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharedailyhistory',
            old_name='open',
            new_name='first',
        ),
    ]
