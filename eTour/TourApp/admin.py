from django.contrib import admin

from TourApp.models import Park_bookings,Hotels_bookings,category,hotels,status,users,tourguide,destinations
# Register your models here.

admin.site.register(Hotels_bookings )
admin.site.register(Park_bookings )
admin.site.register( category)
admin.site.register( hotels)
admin.site.register( status)
# admin.site.register( users)
admin.site.register( tourguide)
admin.site.register(destinations)