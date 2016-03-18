# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_address_postal_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([('name', 'country', 'code')]),
        ),
    ]
