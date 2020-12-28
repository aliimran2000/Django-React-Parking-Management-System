# Generated by Django 3.1.3 on 2020-12-11 20:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20201211_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Due_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 8, 20, 15, 46, 682185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='membership',
            name='Approved_By',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authentication.employee'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='Valid_To',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 20, 15, 46, 681337, tzinfo=utc)),
        ),
    ]
