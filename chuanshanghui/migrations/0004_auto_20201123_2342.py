# Generated by Django 3.1.1 on 2020-11-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chuanshanghui', '0003_auto_20201123_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityinfo',
            name='act_details',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='activityinfo',
            name='act_held_loca',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='activityinfo',
            name='act_held_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='activityinfo',
            name='act_participant',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
