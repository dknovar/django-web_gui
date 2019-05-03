from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recents/$', views.recents),
    url(r'^daftar/$', views.daftar),
    url(r'^lupapass/$', views.lupapass),
    url(r'^$', views.index),
]