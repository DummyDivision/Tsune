# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deck'
        db.create_table(u'cardbox_deck', (
            ('ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'cardbox', ['Deck'])

        # Adding model 'Card'
        db.create_table(u'cardbox_card', (
            ('ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deck', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cardbox.Deck'])),
            ('front', self.gf('markitup.fields.MarkupField')(no_rendered_field=True)),
            ('back', self.gf('markitup.fields.MarkupField')(no_rendered_field=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('_back_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_front_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'cardbox', ['Card'])


    def backwards(self, orm):
        # Deleting model 'Deck'
        db.delete_table(u'cardbox_deck')

        # Deleting model 'Card'
        db.delete_table(u'cardbox_card')


    models = {
        u'cardbox.card': {
            'ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'object_name': 'Card'},
            '_back_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_front_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'back': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deck': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cardbox.Deck']"}),
            'front': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True'})
        },
        u'cardbox.deck': {
            'ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'object_name': 'Deck'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cardbox']