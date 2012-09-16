# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'User'
        db.create_table('gaclient_user', (
            ('creation_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 16, 0, 0, 0, 783204))),
            ('analytics_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('gaclient', ['User'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'User'
        db.delete_table('gaclient_user')
    
    
    models = {
        'gaclient.user': {
            'Meta': {'object_name': 'User'},
            'analytics_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 16, 0, 0, 0, 783204)'})
        }
    }
    
    complete_apps = ['gaclient']
