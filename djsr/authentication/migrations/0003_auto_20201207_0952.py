# Generated by Django 3.1.3 on 2020-12-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20201207_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='DateOfBirth',
            field=models.DateField(blank=True, default='2000-01-01', null=True),
        ),
    ]