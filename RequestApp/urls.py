# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 00:12:19 2023

@author: xcham
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.PendingRequestView, name='PendingRequest'),
]