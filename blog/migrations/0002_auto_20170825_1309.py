# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='fecha_creacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='fecha_publicacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
    ]
