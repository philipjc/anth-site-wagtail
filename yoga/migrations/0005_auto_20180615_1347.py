# Generated by Django 2.0.5 on 2018-06-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0004_yogalesson_loc_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='yogalesson',
            name='lesson_additional_desc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='yogalesson',
            name='lesson_duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='yogalesson',
            name='lesson_price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]