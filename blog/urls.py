# import django's url function
from django.conf.urls import url
# import all of our views from the blog application
from . import views

urlpatterns = [
  url(r'^$', views.post_list, name='post_list'),
  url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]