from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(('reservation.urls','reservation'), namespace='reservation')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]
