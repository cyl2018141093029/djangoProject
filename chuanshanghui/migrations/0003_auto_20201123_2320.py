# Generated by Django 3.1.1 on 2020-11-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chuanshanghui', '0002_auto_20201123_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityinfo',
            name='act_details',
            field=models.CharField(max_length=5000),
        ),
    ]