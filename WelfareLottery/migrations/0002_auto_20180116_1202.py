# Generated by Django 2.0.1 on 2018-01-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WelfareLottery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welfarelottery',
            name='bonus',
            field=models.CharField(max_length=300, verbose_name='开奖信息'),
        ),
    ]