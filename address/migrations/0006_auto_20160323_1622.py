# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_auto_20160318_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='route',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
