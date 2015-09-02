# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='custom_data',
            field=jsonfield.fields.JSONField(default={}, blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='custom_settings',
            field=jsonfield.fields.JSONField(default={}, blank=True),
        ),
    ]
