# Generated by Django 2.0.5 on 2018-06-08 18:43

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_homepage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())], icon='pilcrow', label='Single Column'))], blank=True),
        ),
    ]
