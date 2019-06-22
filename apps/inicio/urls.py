from django.conf.urls import url,include
from apps.inicio.views import home

urlpatterns = [
    url(r'^$', home,name="home"),
]