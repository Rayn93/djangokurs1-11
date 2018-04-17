from django.conf.urls import url
from .views import RestaurantsListView, RestaurantsDetailView, RestaurantCreateView, RestaurantUpdateView



urlpatterns = [
    url(r'^create$', RestaurantCreateView.as_view(), name='create'),
    # url(r'^restaurants/(?P<slug>\w+)$', RestaurantsListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantsDetailView.as_view(), name='detail'),
    url(r'^update/(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='update'),
    url(r'^$', RestaurantsListView.as_view(), name='list'),
]
