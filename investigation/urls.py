from django.urls import path
from .views import AirtableWebhookView

urlpatterns = [
    path('airtable-webhook/', AirtableWebhookView.as_view(), name='airtable-webhook'),
]
