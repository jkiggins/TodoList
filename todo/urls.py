from django.conf.urls import url

from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^(?P<order>|[a-z]+)$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/detail/', views.detail, name='detail'),
    url(r'^newtodo/$', views.newtodo, name='newtodo'),
    url(r'^(?P<pk>[0-9]+)/edittodo/', views.edittodo, name='edittodo'),
    url(r'^(?P<pk>[0-9]+)/delete/', views.delete, name='delete')
]