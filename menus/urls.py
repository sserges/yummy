from django.conf.urls import url


from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
    item_detail,
)
urlpatterns = [
    url(r'^create/$',  ItemCreateView.as_view(), name='create'),
    #url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    url(r'^detail/(?P<id>\d+)/$', item_detail, name='public_detail'),
    url(r'$', ItemListView.as_view(), name='list'),
]
