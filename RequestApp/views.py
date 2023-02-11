from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RequestSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
import os
from BackOfTheNapkin.InvestigationApp.models import CoreModel



class FormRequestView(APIView):
    
    """
    A view that returns a templated HTML representation a user request.
    """
    queryset = CoreModel.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'request.html'
    
    #Action to be done when form data is submitted
    def post(self, request, *args, **kwargs):
        
        serializer = RequestSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        pk=request["id"]

        user = request["fields"]["user"]

        what = request["fields"]["what"]
        who = request["fields"]["who"]
            

        core_request=CoreModel(request_id = pk,
                               user = user,
                               what = what,
                               who = who)

        core_request.save()
        
        return render

    # Method called when form is first displayed
    def get(self,request,*args,**kwargs):
        
        blank_request = get_object_or_404(CoreModel,pk)
        serializer = RequestSerializer()

        return Response({'serializer':serializer})
    


