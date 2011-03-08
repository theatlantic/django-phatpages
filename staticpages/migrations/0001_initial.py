# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'FatPage'
        db.create_table('django_flatpage', (
            ('registration_required', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('template_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('content', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('staticpages', ['FatPage'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'FatPage'
        db.delete_table('django_flatpage')
    
    
    models = {
        'staticpages.fatpage': {
            'Meta': {'object_name': 'FatPage', 'db_table': "'django_flatpage'"},
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['staticpages']
