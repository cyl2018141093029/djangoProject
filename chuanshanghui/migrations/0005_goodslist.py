# Generated by Django 3.1.2 on 2020-11-10 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chuanshanghui', '0004_auto_20201109_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goodslist',
            fields=[
                ('Goods_name', models.AutoField(primary_key=True, serialize=False)),
                ('Goods_price', models.FloatField(blank=True, null=True)),
                ('Goods_qua', models.FloatField(blank=True, null=True)),
                ('Goods_total', models.FloatField(blank=True, null=True)),
                ('beizhu', models.CharField(max_length=500)),
                ('fund_for_act', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chuanshanghui.activityinfo')),
            ],
        ),
    ]