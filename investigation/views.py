from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import GPTRequest


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
