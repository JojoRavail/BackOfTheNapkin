# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:47:35 2023

@author: xcham
"""
from rest_framework import serializers
from BackOfTheNapkin.InvestigationApp.models import CoreModel


class RequestSerializer(serializers.ModelSerializer):
    
       
    class Meta:
        model = CoreModel
        fields = ['user','request_field_1', 'request_field_2']