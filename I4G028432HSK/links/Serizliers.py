from rest_framework import serializers
from .models import Links

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        models = Links
        fields = "__all__"