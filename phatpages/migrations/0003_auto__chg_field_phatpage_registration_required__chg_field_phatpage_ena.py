# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'PhatPage.registration_required'
        db.alter_column('django_flatpage', 'registration_required', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'PhatPage.enable_comments'
        db.alter_column('django_flatpage', 'enable_comments', self.gf('django.db.models.fields.BooleanField')(blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'PhatPage.registration_required'
        db.alter_column('django_flatpage', 'registration_required', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'PhatPage.enable_comments'
        db.alter_column('django_flatpage', 'enable_comments', self.gf('django.db.models.fields.BooleanField')())
    
    
    models = {
        'phatpages.phatpage': {
            'Meta': {'object_name': 'PhatPage', 'db_table': "'django_flatpage'"},
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'excerpt': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['phatpages']
