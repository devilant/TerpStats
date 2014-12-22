from django.conf.urls import patterns, url
from LineupStats import views

urlpatterns = patterns('',
	url(r'^(?P<season>[0-9]*[-]*[0-9]*)$', views.index, name='index'),
	url(r'^about', views.about, name='about'),
	url(r'^filter/(?P<season>\S*)', views.filter, name='filter'))