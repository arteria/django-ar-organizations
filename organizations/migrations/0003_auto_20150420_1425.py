# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20150420_1420'),
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
