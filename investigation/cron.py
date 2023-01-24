from django_cron import CronJobBase, Schedule
import requests
from .models import CoreModel
from .serializers import GPTRequestSerializer

gpt_context="some context for GPT"
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'investigation.my_cron_job'    # a unique code

    def do(self):
        
        #Step 1: query database were "answered"=False
        #Step 2: Iterate through each line to obtain data
        #Step 3: Create the request payload
        #Step 4: Send request
        #Step 5: Update model
        
        unanswered_requests=CoreModel.objects.filter(answered=False)
        index= [line.request_id for line in unanswered_requests]

        for i  in index:
        
            gpt_script = f"some text with {unanswered_requests.get(request_id=i).what} that can be used to send a request to {unanswered_requests.get(request_id=i).who}"
            gpt_serializer=GPTRequestSerializer(script=gpt_script,context=gpt_context)
            json = JSONRenderer().render(gpt_serializer.data)

