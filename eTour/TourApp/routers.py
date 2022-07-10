from atexit import register
from rest_framework import routers

from .views import (
    park_reservations,
    Hotel_reservations,
    cartView
)


p_bookings = routers.DefaultRouter()
p_bookings.register('park-bookings', park_reservations, basename= 'Park bookings')

h_bookings = routers.DefaultRouter()
h_bookings.register('hotel-bookings', Hotel_reservations, basename = "Hotel reservations")

cart_router = routers.DefaultRouter()
cart_router.register('cart', cartView, basename= 'cart')