# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Investor'
        db.create_table(u'advisor_investor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('risk_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('income', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'advisor', ['Investor'])

        # Adding M2M table for field groups on 'Investor'
        m2m_table_name = db.shorten_name(u'advisor_investor_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('investor', models.ForeignKey(orm[u'advisor.investor'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['investor_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Investor'
        m2m_table_name = db.shorten_name(u'advisor_investor_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('investor', models.ForeignKey(orm[u'advisor.investor'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['investor_id', 'permission_id'])

        # Adding model 'AssetType'
        db.create_table(u'advisor_assettype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'advisor', ['AssetType'])

        # Adding model 'Investment'
        db.create_table(u'advisor_investment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('asset_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='investments', to=orm['advisor.AssetType'])),
            ('fees', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=10)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'advisor', ['Investment'])

        # Adding model 'Portfolio'
        db.create_table(u'advisor_portfolio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('investor', self.gf('django.db.models.fields.related.OneToOneField')(related_name='portfolio', unique=True, to=orm['advisor.Investor'])),
        ))
        db.send_create_signal(u'advisor', ['Portfolio'])

        # Adding M2M table for field investments on 'Portfolio'
        m2m_table_name = db.shorten_name(u'advisor_portfolio_investments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolio', models.ForeignKey(orm[u'advisor.portfolio'], null=False)),
            ('investment', models.ForeignKey(orm[u'advisor.investment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['portfolio_id', 'investment_id'])


    def backwards(self, orm):
        # Deleting model 'Investor'
        db.delete_table(u'advisor_investor')

        # Removing M2M table for field groups on 'Investor'
        db.delete_table(db.shorten_name(u'advisor_investor_groups'))

        # Removing M2M table for field user_permissions on 'Investor'
        db.delete_table(db.shorten_name(u'advisor_investor_user_permissions'))

        # Deleting model 'AssetType'
        db.delete_table(u'advisor_assettype')

        # Deleting model 'Investment'
        db.delete_table(u'advisor_investment')

        # Deleting model 'Portfolio'
        db.delete_table(u'advisor_portfolio')

        # Removing M2M table for field investments on 'Portfolio'
        db.delete_table(db.shorten_name(u'advisor_portfolio_investments'))


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'risk_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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