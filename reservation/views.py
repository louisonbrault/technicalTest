from reservation.models import Reservation, Room
from reservation.serializers import ReservationSerializer
from reservation.serializers import RoomSerializer
from rest_framework import generics
from reservation.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from reservation.permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from django.forms import ModelForm
from .forms import ReservationForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

import logging

def index(request):
    room_list = Room.objects.order_by('-name')[:5]
    context = {'room_list': room_list}
    return render(request, 'reservation/index.html', context)

def reserve(request):
    form = ReservationForm()
    context = { 'form':form, }
    return render(request, 'reservation/reserve.html', context)

def myReservation(request):
    reservation_list = Reservation.objects.filter(owner=request.user)
    context = {'reservation_list': reservation_list}
    return render(request, 'reservation/myReservation.html', context)

class ReservationList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
