from django import urls
from django.conf.urls import *
from TourApp.views import *
from django.urls import path,include
from django.contrib import admin
from .routers import h_bookings,p_bookings, cart_router,destination,hotel



urlpatterns = [
    # path('users',ListUsers.as_view(),name='users'),
    # path('users/<int:pk>',DetailUsers.as_view() ,name = 'singleuser'),

    # path('destinations',ListDestination.as_view(), name='destination'),
    path('Destinations/([0-9]+)',DetailDestination.as_view(), name='singledestination'),

    # path('hotels',ListHotel.as_view(), name='hotel'),
    # path('hotels/([0-9]+)',DetailHotel.as_view(), name='singlehotel'),

    path('categories',ListCategory.as_view(), name='category'),
    path('categories/([0-9]+)',DetailCategory.as_view(), name='singlecategory'),

    path('status',ListStatus.as_view(), name='status'),
    path('status/([0-9]+)',DetailStatus.as_view(), name='singlestatus'),

    path('testimonials', TestimonialsView.as_view(), name= ' Testimonials'),

    path('user/', include(h_bookings.urls)),
    path('user/', include(p_bookings.urls)),

    path('user/',include(cart_router.urls)),

    path('', include(destination.urls)),

    path('', include(hotel.urls)),

]

