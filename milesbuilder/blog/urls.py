
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='all'),
    url(r'^detail/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='detail'),
    url(r'^create/$', views.PostCreate.as_view(), name='create'),
    url(r'^drafts/$', views.DraftList.as_view(), name='drafts'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.PostDelete.as_view(), name='delete'),
    url(r'^publish/(?P<pk>\d+)/$', views.publish, name='publish'),
]
