from django.conf.urls import include, url


from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from core import views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'itemlist', views.ItemListViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


