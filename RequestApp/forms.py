# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 23:43:49 2023

@author: xcham
"""

from django import forms

class RequestForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=100)
    first_name = forms.CharField(label='Whats your name?',max_lenght=50)
    surname = forms.CharField(label='Whats your surname?',max_lenght=50)
    request_field_1=forms.CharField(label='Her/His last message',max_lenght=500)
    request_field_2=forms.CharField(label='Your last message',max_lenght=500)