from django.conf.urls import url

from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/detail/', views.detail, name='detail'),
    url(r'^newtodo/$', views.newtodo, name='newtodo'),
    url(r'^(?P<pk>[0-9]+)/edittodo/', views.edittodo, name='edittodo'),
]