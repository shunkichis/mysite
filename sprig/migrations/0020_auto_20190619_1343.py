# Generated by Django 2.0 on 2019-06-19 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprig', '0019_auto_20190607_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 14, 43, 24, 532087), verbose_name='納期'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 13, 43, 24, 531860), null=True, verbose_name='着手日時'),
        ),
    ]
