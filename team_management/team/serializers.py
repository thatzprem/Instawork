from team.models import Member
import logging
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        
    def validate(self,data):
        return data

        