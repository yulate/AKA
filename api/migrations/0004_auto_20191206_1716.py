# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191007_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_message',
            name='data_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
