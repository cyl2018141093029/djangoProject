# Generated by Django 3.1.2 on 2020-11-09 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chuanshanghui', '0003_auto_20201105_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityinfo',
            name='act_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='reim_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
