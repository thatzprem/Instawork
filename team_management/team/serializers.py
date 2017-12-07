from team.models import Member
import logging
from rest_framework import serializers
from localflavor.us.forms import USPhoneNumberField
from django.core.exceptions import ValidationError

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__' 
    
    def validate_phone_number(self, value):
        value = USPhoneNumberField().clean(value)
        return value
        