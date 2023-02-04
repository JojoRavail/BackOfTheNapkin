from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import GPTRequest


class GPTView(View):

    def post(self, request, *args, **kwargs):
        

    def get(self, request, *args, **kwargs):
