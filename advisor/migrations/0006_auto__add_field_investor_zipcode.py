# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Investor.zipcode'
        db.add_column(u'advisor_investor', 'zipcode',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=5, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Investor.zipcode'
        db.delete_column(u'advisor_investor', 'zipcode')


    models = {
        u'advisor.assettype': {
            'Meta': {'object_name': 'AssetType'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'advisor.investment': {
            'Meta': {'object_name': 'Investment'},
            'asset_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'investments'", 'to': u"orm['advisor.AssetType']"}),
            'fees': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'advisor.investor': {
            'Meta': {'object_name': 'Investor'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '18', 'null': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'disposible_monthly': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'housing': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'risk_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '5', 'null': 'True'})
        },
        u'advisor.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'portfolios'", 'symmetrical': 'False', 'to': u"orm['advisor.Investment']"}),
            'investor': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'portfolio'", 'unique': 'True', 'to': u"orm['advisor.Investor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['advisor']