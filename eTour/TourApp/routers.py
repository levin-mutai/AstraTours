from atexit import register
from rest_framework import routers

from .views import (
    park_reservations,
    Hotel_reservations,
    cartView,
    DestinationView,
    DetailHotel
)


p_bookings = routers.DefaultRouter()
p_bookings.register('park-bookings', park_reservations, basename= 'park_bookings')

h_bookings = routers.DefaultRouter()
h_bookings.register('hotel-bookings', Hotel_reservations, basename = "hotels")

cart_router = routers.DefaultRouter()
cart_router.register('cart', cartView, basename= 'cart')

destination = routers.DefaultRouter()
destination.register('destinations', DestinationView, basename= 'destinations')

hotel = routers.DefaultRouter()
hotel.register('hotels', DetailHotel , basename='listed_hotels')

