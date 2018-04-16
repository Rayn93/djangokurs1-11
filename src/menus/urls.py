from django.conf.urls import url
from .views import ItemCreateView, ItemDetailView, ItemListView, ItemUpdateView



urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),
    url(r'^create$', ItemCreateView.as_view(), name='create'), #restaurant_createview
    url(r'^update/(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='update'),
    url(r'^$', ItemListView.as_view(), name='list'),
]
