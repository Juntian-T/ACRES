from django.conf.urls import url

from . import views

# This file defines all the URL related to the web application. 
# URL samples are in the commments

urlpatterns = [
	# .../FarmInfo
    url(r'^$', views.index, name='index'),
    
    # .../FarmInfo/1  etc.
    url(r'^(?P<farm_id>[0-9]+)/$', views.detail, name='detail'),

    # .../FarmInfo/addCrop
    url(r'^addCrop/$', views.addCrop, name='addCrop'),

    # .../FarmInfo/addFarm
    url(r'^addFarm/$', views.addFarm, name='addFarm'),

    # .../FarmInfo/addVisit
    url(r'^addVisit/(?P<farm_id>[0-9]+)/$', views.addVisit, name='addVisit'),
    
    # .../FarmInfo/viewVisits
    url(r'^viewVisits/(?P<farm_id>[0-9]+)/$', views.viewVisits, name='viewVisits'),
    
    # .../FarmInfo/visitDetail
    url(r'^visitDetail/1/$', views.visitDetail, name='visitDetail'),
]