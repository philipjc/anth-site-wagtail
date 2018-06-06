# Generated by Django 2.0.5 on 2018-06-06 09:23

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0020_add-verbose-name'),
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Health Category',
            },
        ),
        migrations.CreateModel(
            name='HealthTreatment',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('treatment_title', models.CharField(max_length=200, null=True)),
                ('treatment_desc', models.CharField(max_length=500, null=True)),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, to='health.HealthCategory')),
                ('treatment_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Health Treatment',
            },
            bases=('wagtailcore.page',),
        ),
    ]
