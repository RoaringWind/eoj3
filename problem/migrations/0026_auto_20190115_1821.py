# Generated by Django 2.1.3 on 2019-01-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0025_auto_20190115_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='judging_memory_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='judging_time_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='package_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]