
from inspect import formatannotationrelativeto
from pyexpat import model
from django.db.models import fields
from rest_framework import serializers
from TourApp.models import Park_bookings,Hotels_bookings, Testimonials,category,hotels,status,users,tourguide,destinations,cart

class usersSerializer (serializers.ModelSerializer):
    class Meta:
        model= users
        fields = (
            'userId',
            'firstname',
            'lastname',
            'nationality',
            'languages',
            'photo',
            'email',
            'contact',
            'username',
        )

class destinationsSerializer (serializers.ModelSerializer):
    class Meta:
        model= destinations
        fields = (
            'destinationId',
            'name',
            'description',
            'longitude',
            'latitude',
            'categori',
            'price',
            'imageurl',
            'url',
            'rating'
        )

class hotelsSerializer (serializers.ModelSerializer):
    class Meta:
        model= hotels
        fields = (
            'hotelId',
            'name',
            'description',
            'location',
            'city',
            'price',
            'imageurl',
            'url',
            'rating'
        )

class tourguideSerializer (serializers.ModelSerializer):
    class Meta:
        model= tourguide
        fields = ('__all__')


class categorySerializer (serializers.ModelSerializer):
    class Meta:
        model= category
        fields = (
            'categories',
        )

class statusSerializer (serializers.ModelSerializer):
    class Meta:
        model= status
        fields = (
            'state',
        )


class Park_bookingSerializer (serializers.ModelSerializer):
    class Meta:
        model= Park_bookings
        fields = ('__all__')

class Hotels_bookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Hotels_bookings
        fields = ('__all__')

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ("__all__")

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ('__all__')