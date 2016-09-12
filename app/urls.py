from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^second', views.second, name='second'),
    url(r'^profile', views.profile, name='profile'),
]
