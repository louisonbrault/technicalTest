from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from reservation import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reserve/$', views.reserve, name='reserve'),
    url(r'^reservations/$', views.ReservationList.as_view()),
    url(r'^reservations/(?P<pk>[0-9]+)/$', views.ReservationDetail.as_view()),
    url(r'^myreservation/$', views.myReservation, name='myReservation'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
