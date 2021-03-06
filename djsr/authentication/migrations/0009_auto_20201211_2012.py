# Generated by Django 3.1.3 on 2020-12-11 20:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20201211_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Due_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 8, 20, 12, 8, 417670, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='membership',
            name='Member_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.member'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='Valid_To',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 20, 12, 8, 416831, tzinfo=utc)),
        ),
    ]
