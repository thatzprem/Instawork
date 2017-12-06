from django.shortcuts import render
from django.http import HttpResponse
from rest_framework_tracking.mixins import LoggingMixin
from team.serializers import MemberSerializer
from team.models import Member
from rest_framework import generics, filters, status
from rest_framework.viewsets import ModelViewSet

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the team index.")

class MemberMixin(LoggingMixin):
       
    serializer_class = MemberSerializer
    queryset = Member.objects.all()   
    filter_backends = (filters.OrderingFilter,)
            
    def get_serializer_class(self):
            return MemberSerializer
            
    def get_queryset(self): 
        return  Member.objects.all()
    
class MemberViewSet(MemberMixin, ModelViewSet):
        
    def create(self, request, *args, **kwargs):        
        return ModelViewSet.create(self, request, *args, **kwargs)
                
    def update(self, request, *args, **kwargs):
        return ModelViewSet.update(self, request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return ModelViewSet.destroy(self, request, *args, **kwargs)
