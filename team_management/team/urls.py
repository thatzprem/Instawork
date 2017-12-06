from django.conf.urls import url, patterns
from . import views
from rest_framework.routers import DefaultRouter

member_router = DefaultRouter()
member_router.register(r'', views.MemberViewSet)

urlpatterns = patterns('',
    url(r'^$',views.index,name="index"),        
    )
