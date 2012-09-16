# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'User.expiration_time'
        db.add_column('gaclient_user', 'expiration_time', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=30, decimal_places=24), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'User.expiration_time'
        db.delete_column('gaclient_user', 'expiration_time')
    
    
    models = {
        'gaclient.user': {
            'Meta': {'object_name': 'User'},
            'analytics_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 16, 0, 11, 43, 989227)'}),
            'expiration_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '24'})
        }
    }
    
    complete_apps = ['gaclient']
