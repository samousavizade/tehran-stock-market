# Generated by Django 3.0.5 on 2020-05-18 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0006_auto_20200518_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharedailyhistory',
            old_name='yesterday',
            new_name='open',
        ),
    ]
