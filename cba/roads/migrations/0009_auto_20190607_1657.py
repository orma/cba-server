# Generated by Django 2.2.2 on 2019-06-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0008_auto_20190607_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='trafficlevel',
            name='traffic_from',
            field=models.IntegerField(blank=True, null=True, verbose_name='traffic from'),
        ),
        migrations.AddField(
            model_name='trafficlevel',
            name='traffic_to',
            field=models.IntegerField(blank=True, null=True, verbose_name='traffic to'),
        ),
    ]
