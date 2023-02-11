from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class GPTRequestSerializer(serializers.Serializer):
    script = serializers.CharField(max_length=1000)
    context = serializers.CharField(max_length=1000)
    