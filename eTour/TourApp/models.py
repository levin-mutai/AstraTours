
from datetime import datetime
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DurationField, EmailField
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from accounts.models import Accounts
from django.utils import timezone
from django.urls import reverse
# from sqlalchemy import null

# Create your models here.

class users (models.Model):
    userId = models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    nationality = models.CharField(max_length=100)
    languages = models.CharField(max_length=250)
    photo = models.ImageField(null=True,upload_to='static')
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

class admin (models.Model):
    adminId = models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    photo = models.ImageField(null=True,upload_to='static')
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

class category(models.Model):
    categories = models.CharField(primary_key=True,max_length=150)

# def __str__(    self): 
#         return category.categories

class destinations (models.Model):
    destinationId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500,default='')
    name= models.CharField(max_length=150)
    longitude = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    categori = models.ForeignKey(category, on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField()
    imageurl = models.URLField()
    url = models.CharField(max_length=100,default='')
    rating = models.IntegerField(default=3)

class hotels (models.Model):
    hotelId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500,default='')
    name= models.CharField(max_length=150)
    location = models.CharField(max_length=250, default= "")
    city = models.CharField(max_length=250, default= "")
    rating = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    imageurl = models.URLField()
    url = models.CharField(max_length=100,default='')
    rating = models.IntegerField(default=3)

    def __str__(self):
        return self.name

        
class status(models.Model):
    state = models.CharField(primary_key=True,max_length=150)

    def __str__(self): 
        return self.state

class tourguide (models.Model):
    Id = models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    languages = models.CharField(max_length=250)
    photo = models.ImageField(null=True,upload_to='static')
    email = models.EmailField()
    speciality = models.ForeignKey(category, related_name="speciality",on_delete=models.DO_NOTHING)
    contact = models.CharField(max_length=100)
    status = models.ForeignKey(status, related_name="status",on_delete=models.DO_NOTHING)

class Park_bookings(models.Model):
    Id = models.AutoField(primary_key=True)
    userID = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    tourguideId = models.ForeignKey(tourguide, on_delete=models.DO_NOTHING)
    destinationId= models.ForeignKey(destinations,  on_delete=models.DO_NOTHING)
    bill = models.PositiveIntegerField() 
    # state = models.Choices() #active,cancelled,Visited

class Hotels_bookings(models.Model):
    Id = models.AutoField(primary_key=True)
    userID = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    tourguideId = models.ForeignKey(tourguide, on_delete=models.DO_NOTHING)
    from_date= models.DateField(default=timezone.now)
    to_date= models.DateField( )
    hotel = models.ForeignKey(hotels,  on_delete=models.DO_NOTHING)
    bill = models.PositiveIntegerField() 
    # state = models.Choices() #active,cancelled,Visited


class Testimonials(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    user_profile = models.URLField( max_length=200)
    testimony = models.CharField(max_length=600)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.user_name


class cart (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    hotel = models.ForeignKey(hotels, on_delete=models.DO_NOTHING,blank=True,null=True)
    park = models.ForeignKey(destinations,  on_delete=models.DO_NOTHING, blank=True, null= True)


    class Meta:
        verbose_name = "cart"
        verbose_name_plural = "carts"

   

class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    hotel = models.ForeignKey(hotels, on_delete=models.DO_NOTHING,blank=True,null=True)
    image = models.URLField( max_length=200)
    tag = models.CharField( max_length=50)
    

    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Experiences")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Experience_detail", kwargs={"pk": self.pk})

