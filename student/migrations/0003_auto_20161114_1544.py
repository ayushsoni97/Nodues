# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20161114_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkbox',
            old_name='stud',
            new_name='cred',
        ),
    ]