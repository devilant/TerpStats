from django.conf.urls import patterns, url
from LineupStats import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about', views.about, name='about'),
	url(r'^filter', views.filter, name='filter'))