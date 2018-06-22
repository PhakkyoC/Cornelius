from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup$', views.create_account, name='signup'),
    url(r'^login', views.login_user, name='login'),
    url(r'^logout', views.logout_fct, name='logout'),
    url(r'^create_event', views.create_event, name='create_event'),
    url(r'^getplace', views.getplace, name='getplace')
]
