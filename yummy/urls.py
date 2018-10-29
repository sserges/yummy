import os

from django.conf.urls import url, include, handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from menus.views import HomeView, AllUserRecentItemListView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

handler404 = 'yummy.views.handler404'
handler500 = 'yummy.views.handler500'

ADMIN_URL = os.environ.get('ADMIN_URL') or r'^admin/'

urlpatterns = [
    url(ADMIN_URL, admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^recent/$', AllUserRecentItemListView.as_view(), name='recent'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^recipes/', include('recipes.urls', namespace='recipes')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    # url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    # url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]


if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)