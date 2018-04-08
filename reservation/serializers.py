from rest_framework import serializers
from reservation.models import Room, Reservation
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    reservations = serializers.PrimaryKeyRelatedField(many=True, queryset=Reservation.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'reservations')


class ReservationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Reservation
        fields = ('id', 'reason', 'startTime', 'endTime', 'room','owner')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','name')
