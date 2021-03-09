# -*- coding: utf-8 -*-
from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100, verbose_name='URL', db_index=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('excerpt', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('enable_comments', models.BooleanField(default=False, verbose_name='enable comments')),
                ('template_name', models.CharField(help_text="Example: 'staticpages/contact_page.html'. If this isn't provided, the system will use the default.", max_length=70, verbose_name='template name', blank=True)),
                ('registration_required', models.BooleanField(default=False, help_text='If this is checked, only logged-in users will be able to view the page.', verbose_name='registration required')),
                ('site', models.ForeignKey(to='sites.Site', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ('url',),
                'db_table': 'django_flatpage',
                'verbose_name': 'static page',
                'verbose_name_plural': 'static pages',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='phatpage',
            unique_together=set([('site', 'url')]),
        ),
    ]
