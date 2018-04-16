from django.conf.urls import url
from .views import RestaurantsListView, RestaurantsDetailView, restaurant_createview, RestaurantCreateView



urlpatterns = [
    url(r'^create$', RestaurantCreateView.as_view(), name='create'), #restaurant_createview
    # url(r'^restaurants/(?P<slug>\w+)$', RestaurantsListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantsDetailView.as_view(), name='detail'),
    url(r'^$', RestaurantsListView.as_view(), name='list'),
]
