from django.conf.urls import url
from django.contrib import admin

from .views import FilmListAPIView
from .views import FilmDetailAPIView


urlpatterns = [
    url(r'^$', FilmListAPIView.as_view(),name='list'),
    url(r'^(?P<slug>[\w-]+)/$', FilmDetailAPIView.as_view(),name ='detail'),

]
