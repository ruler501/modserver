# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod',
            name='version',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
    ]
