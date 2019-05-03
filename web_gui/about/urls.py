from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recents/$', views.recents),
    url(r'^$', views.index),
]