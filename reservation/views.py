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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

class ReservationList(APIView):
 """
 List all reservations, or create a new one.
 """
 permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
 def get(self, request, format=None):
     reservations = Reservation.objects.all()
     serializer = ReservationSerializer(reservations, many=True)
     return Response(serializer.data)

 def post(self, request, format=None):
     serializer = ReservationSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save(owner=self.request.user)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
