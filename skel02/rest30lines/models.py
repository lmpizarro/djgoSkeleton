# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.conf import settings

UPLOADS_DIR = getattr(settings, "UPLOADS_DIR", "uploads")

class File(models.Model):
    file = models.FileField(upload_to=UPLOADS_DIR)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)

