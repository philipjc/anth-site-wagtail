# Generated by Django 2.0.5 on 2018-06-08 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='name',
        ),
    ]