from django.conf.urls import patterns, url

from laws import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index')
)
