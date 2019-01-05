# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import migrations
from django.contrib.auth.models import Permission


def is_valid_model(content_type):
    return content_type.model_class() is not None


def add_models_export_permissions(apps, schema_editor):
    valid_models = list(filter(lambda ct: is_valid_model(ct), ContentType.objects.all()))
    for ct in valid_models:
        Permission.objects.create(
            name='Can export ' + ct.name,
            content_type=ct,
            codename='export_' + ct.model
        )


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(add_models_export_permissions),
    ]
