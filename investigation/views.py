from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import GPTRequest
import os
from pyairtable import Table


#In this example, I've created a AirtableWebhookView class that inherits from View, and overrides the post method to handle incoming POST requests.
#This view deserialize the request data into a python object, extract the relevant data, create a GPTRequest instance and saves it to the database.

class AirtableWebhookView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        # Extract the data from the request
        what = data.get('What')
        who = data.get('Who')
        # Create a GPTRequest instance
        gpt_request = GPTRequest(what=what, who=who)
        gpt_request.save()
        # Perform any additional logic or calculations as necessary
        return JsonResponse({'status': 'success'})

    def get(self,request,*args,**kwargs):
        api_key = os.environ["AIRTABLE_API_KEY"]
        table_id = "tblPv7dUE78OLykf9"
        base_id = "app8F4rWKdCgsLgNC"
        url = "https://api.airtable.com/v0/" + api_key + "/" + table_name
        requests_to_answer=Table(api_key,base_id,table_id).


