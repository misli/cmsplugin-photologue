# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-04 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photologue', '0011_auto_20190223_2138'),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotologueGallery',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_photologue_photologuegallery', serialize=False, to='cms.CMSPlugin')),
                ('display_link', models.BooleanField(default=False, verbose_name='Display link')),
                ('order', models.CharField(choices=[('gallery', 'Gallery Order'), ('latest', 'Latest first'), ('oldest', 'Oldest first'), ('random', 'Random order')], default='gallery', max_length=8, verbose_name='order')),
                ('limit', models.PositiveIntegerField(default=0, help_text='0 means no limit')),
                ('template', models.CharField(choices=[('coccinella', 'coccinella')], default='coccinella', help_text='The template used to render the gallery.', max_length=100, verbose_name='template')),
                ('display_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='photologue.PhotoSize', verbose_name='Display size')),
                ('link_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='photologue.PhotoSize', verbose_name='Link size')),
                ('obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photologue.Gallery', verbose_name='gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PhotologuePhoto',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_photologue_photologuephoto', serialize=False, to='cms.CMSPlugin')),
                ('display_link', models.BooleanField(default=False, verbose_name='Display link')),
                ('template', models.CharField(choices=[('coccinella', 'coccinella')], default='coccinella', help_text='The template used to render the image.', max_length=100, verbose_name='template')),
                ('display_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='photologue.PhotoSize', verbose_name='Display size')),
                ('link_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='photologue.PhotoSize', verbose_name='Link size')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photologue.Photo', verbose_name='photo')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]