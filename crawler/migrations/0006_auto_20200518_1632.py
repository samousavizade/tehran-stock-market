# Generated by Django 3.0.5 on 2020-05-18 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0005_auto_20200518_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharedailyhistory',
            old_name='tomorrow',
            new_name='close',
        ),
    ]
