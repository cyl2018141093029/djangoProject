# Generated by Django 3.1.2 on 2020-11-12 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chuanshanghui', '0006_auto_20201112_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='astu_num',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='chuanshanghui.dpmembers', to_field='stu_num', verbose_name='任务发布负责人'),
        ),
    ]
