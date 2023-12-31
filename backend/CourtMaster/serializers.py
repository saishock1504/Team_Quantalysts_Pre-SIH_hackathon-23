from rest_framework import serializers
from .models import Case, User

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"