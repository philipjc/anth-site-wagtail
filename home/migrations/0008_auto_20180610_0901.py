# Generated by Django 2.0.5 on 2018-06-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_header',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_intro_header',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
