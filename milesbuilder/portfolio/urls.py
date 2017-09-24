from django.conf.urls import url
from portfolio import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^$', views.ProjectList.as_view(), name='all'),
    url(r'^detail/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='detail'),
    url(r'^create/$', views.ProjectCreate.as_view(), name='create'),
    url(r'^createimage/$', views.ImageCreate.as_view(), name='imagecreate'),
    url(r'^delete/(?P<pk>\d+)/$', views.ProjectDelete.as_view(), name='delete'),
]
