# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404

import modelsMDB as mdb

# Create your views here.





def home_page (request):
    tquery = mdb.DbConn.getAll()
    context = {'data':{'user':'lmpizarro', 'function':'developer', \
            'query': tquery}}
    return render(request, 'myApp01/home_page.html', context)
