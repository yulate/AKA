# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_api_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api_user',
            name='id',
        ),
        migrations.AlterField(
            model_name='api_user',
            name='username',
            field=models.CharField(primary_key=True, max_length=20, serialize=False),
        ),
    ]
