from inspect import formatannotationrelativeto
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

from TourApp.models import category,hotels,status,users,tourguide,destinations,Park_bookings,Hotels_bookings,Testimonials,cart
from TourApp.serializers import  categorySerializer,hotelsSerializer,statusSerializer,usersSerializer,tourguideSerializer,destinationsSerializer,Park_bookingSerializer,Hotels_bookingSerializer,TestimonialSerializer,cartSerializer


        

class ListUsers(generics.ListCreateAPIView):

    queryset= users.objects.all()
    serializer_class = usersSerializer

class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset= users.objects.all()
    serializer_class = usersSerializer


class ListDestination(generics.ListCreateAPIView):
    queryset = destinations.objects.all()
    serializer_class = destinationsSerializer
class DetailDestination(generics.RetrieveUpdateDestroyAPIView):
    queryset = destinations.objects.all()
    serializer_class= destinationsSerializer

class DestinationView(viewsets.ModelViewSet):
    '''
    A class to list all the Destinations listed and also sngly identify a destinaon using a destion id 
    '''
    print('has been')
    serializer_class= destinationsSerializer

    def get_queryset(self):
        specific_destination = destinations.objects.all()
        return specific_destination

    def retrieve(self,request, *args, **kwargs):
        params = kwargs
        queryset = destinations.objects.filter(destinationId = params['pk'])
        serializer = destinationsSerializer(queryset, many=True)
        return Response(serializer.data)

class ListTourGuide(generics.ListCreateAPIView):
    queryset = tourguide.objects.all()
    serializer_class = tourguideSerializer
class DetailTourGuide(generics.RetrieveUpdateDestroyAPIView):
    queryset = tourguide.objects.all()
    serializer_class = tourguideSerializer

class ListHotel(generics.ListCreateAPIView):
    queryset = hotels.objects.all()
    serializer_class = hotelsSerializer

class DetailHotel(viewsets.ModelViewSet):
    '''
    A class to list all the hotels listed and also singly identify a hotel using a  hotelid 
    '''
    serializer_class= hotelsSerializer

    def get_queryset(self):
        specific_hotel = hotels.objects.all()
        return specific_hotel

    def retrieve(self,request, *args, **kwargs):
        params = kwargs
        queryset = hotels.objects.filter(hotelId = params['pk'])
        serializer = hotelsSerializer(queryset, many=True)
        return Response(serializer.data)


class ListCategory(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = categorySerializer
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = categorySerializer

class ListStatus(generics.ListCreateAPIView):
    queryset = status.objects.all()
    serializer_class = statusSerializer

class DetailStatus(generics.RetrieveUpdateDestroyAPIView):
    queryset = status.objects.all()
    serializer_class = statusSerializer

class park_reservations(viewsets.ModelViewSet):
    '''
    Used to store all the list of Game park/reserves booking made
    '''
    serializer_class = Park_bookingSerializer
    
    def get_queryset(self):
        specific_booking = Park_bookings.objects.all()
        return specific_booking

    def retrieve(self,request, *args, **kwargs):
        params = kwargs
        queryset = Park_bookings.objects.filter(userID = params['pk'])
        serializer = Park_bookingSerializer(queryset, many=True)
        return Response(serializer.data)


class Hotel_reservations(viewsets.ModelViewSet):
    '''
    Used to store all the list of hotels booking made
    '''
    serializer_class = Hotels_bookingSerializer
    
    def get_queryset(self):
        specific_booking = Hotels_bookings.objects.all()
        return specific_booking

    def retrieve(self,request, *args, **kwargs):
        params = kwargs
        queryset = Hotels_bookings.objects.filter(userID = params['pk'])
        serializer = Hotels_bookingSerializer(queryset, many=True)
        return Response(serializer.data)

class TestimonialsView(generics.ListCreateAPIView):
    '''
    Lists and allows input of testimonials
    '''
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialSerializer

class cartView(viewsets.ModelViewSet):
    '''
    a simple cart feature to hold all the checked services
    '''
    serializer_class = cartSerializer

    def get_queryset(self):
        specific_booking = cart.objects.all()
        return specific_booking

    def retrieve(self,request, *args, **kwargs):
        params = kwargs
        queryset = cart.objects.filter(user = params['pk'])
        serializer = cartSerializer(queryset, many=True)
        return Response(serializer.data)


    