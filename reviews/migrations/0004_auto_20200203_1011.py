# Generated by Django 2.2.5 on 2020-02-03 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200202_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Accuracy',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='check_in',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='communication',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='location',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.IntegerField(),
        ),
    ]
