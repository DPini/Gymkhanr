from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^Gymcana/(?P<pk>[0-9]+)/$', views.proves_gymcana),
	url(r'^Gymcana/(?P<pk>[0-9]+)/(?P<idprova>[0-9]+)/$', views.detalls_prova),
    ]
