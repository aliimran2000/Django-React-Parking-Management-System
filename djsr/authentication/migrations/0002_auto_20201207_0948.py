# Generated by Django 3.1.3 on 2020-12-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='DateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
