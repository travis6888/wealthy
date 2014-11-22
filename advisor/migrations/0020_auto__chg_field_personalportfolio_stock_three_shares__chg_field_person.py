# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PersonalPortfolio.stock_three_shares'
        db.alter_column(u'advisor_personalportfolio', 'stock_three_shares', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=3))

        # Changing field 'PersonalPortfolio.stock_four_shares'
        db.alter_column(u'advisor_personalportfolio', 'stock_four_shares', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=3))

        # Changing field 'PersonalPortfolio.stock_two_shares'
        db.alter_column(u'advisor_personalportfolio', 'stock_two_shares', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=3))

        # Changing field 'PersonalPortfolio.stock_five_shares'
        db.alter_column(u'advisor_personalportfolio', 'stock_five_shares', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=3))

    def backwards(self, orm):

        # Changing field 'PersonalPortfolio.stock_three_shares'
        db.alter_column(u'advisor_personalportfolio', 'stock_three_shares', self.gf('django.db.models.fields.FloatField')(max_length=100, null=True))

        # Changing field 'PersonalPortfolio.stock_four_shares'
        db.alter_column(u'advisor_personalportfolio', 'stock_four_shares', self.gf('django.db.models.fields.FloatField')(max_length=100, null=True))

        # Changing field 'PersonalPortfolio.stock_two_shares'
        db.alter_column(u'advisor_personalportfolio', 'stock_two_shares', self.gf('django.db.models.fields.FloatField')(max_length=100, null=True))

        # Changing field 'PersonalPortfolio.stock_five_shares'
        db.alter_column(u'advisor_personalportfolio', 'stock_five_shares', self.gf('django.db.models.fields.FloatField')(max_length=100, null=True))

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
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'fees': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '5'}),
            'hidden_symbol': ('django.db.models.fields.TextField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'advisor.investor': {
            'Meta': {'object_name': 'Investor'},
            'after_tax': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'age': ('django.db.models.fields.FloatField', [], {'default': '18', 'null': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'disposible_monthly': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'housing': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'monthly_investment': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '20', 'null': 'True'}),
            'other_costs': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'portfolio_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'risk_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'zipcode': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '5', 'null': 'True'})
        },
        u'advisor.personalportfolio': {
            'Meta': {'object_name': 'PersonalPortfolio'},
            'cost': ('django.db.models.fields.FloatField', [], {'max_length': '90', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'personal_portfolio'", 'to': u"orm['advisor.Investor']"}),
            'stock_five_name': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'stock_five_shares': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '100', 'decimal_places': '3', 'blank': 'True'}),
            'stock_four_name': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'stock_four_shares': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '100', 'decimal_places': '3', 'blank': 'True'}),
            'stock_one_name': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'stock_one_shares': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '100', 'decimal_places': '3', 'blank': 'True'}),
            'stock_three_name': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'stock_three_shares': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '100', 'decimal_places': '3', 'blank': 'True'}),
            'stock_two_name': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'stock_two_shares': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '100', 'decimal_places': '3', 'blank': 'True'})
        },
        u'advisor.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'expected_return': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'portfolios'", 'symmetrical': 'False', 'to': u"orm['advisor.Investment']"}),
            'investor': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'portfolio'", 'unique': 'True', 'to': u"orm['advisor.Investor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'advisor.stocks': {
            'Meta': {'object_name': 'Stocks'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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