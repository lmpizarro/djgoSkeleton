# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# views.py
from .models import File

from .serializers import FileSerializer

from rest_framework.viewsets import ModelViewSet

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

