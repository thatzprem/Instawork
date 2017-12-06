from django.conf.urls import url, patterns
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, url, include

member_router = DefaultRouter()
member_router.register(r'member', views.MemberViewSet)

urlpatterns = patterns('',
    url(r'^$',views.index,name="index"), 
    url(r'^', include(member_router.urls)), 
    )
