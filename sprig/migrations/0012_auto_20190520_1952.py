# Generated by Django 2.0 on 2019-05-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprig', '0011_auto_20190519_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='linker',
        ),
        migrations.RemoveField(
            model_name='step',
            name='loc',
        ),
        migrations.AddField(
            model_name='step',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='step',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
