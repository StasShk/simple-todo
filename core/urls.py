from django.conf.urls import include, url


from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    url(r'^api/$', views.ItemsAll.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)