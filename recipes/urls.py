from django.conf.urls import url

from .views import (
    recipe_create,
    recipe_detail,
)

urlpatterns = [
    url(r'^add/$', recipe_create, name='create'),
    url(r'^(?P<id>\d+)/$', recipe_detail, name='detail'),
]