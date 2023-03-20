from rest_framework import serializers
from Content.models import *

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'title', 'body', 'summary', 'document'
        ]

    