from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    Name=models.CharField('Category', max_length=200, blank=True, null=True, default='Uncategorized' )
    Image=models.ImageField(blank=True, null=True,upload_to='images/', default=None)
    def __str__(self):
        return self.Name



class RenteeUser(models.Model):
    Name= models.CharField('User Name', max_length=120)
    Email=models.EmailField('User Email')

    def __str__(self):
        return self.Name


class Listing(models.Model):
    Owneruser = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=1)
    Name=models.CharField('Listing Name', max_length=120)
    Location= models.CharField('Listing Location', max_length=120)
    Description=models.TextField('Listing Description',null=False, blank=False, max_length=1000, default='In Good Shape')
    # HourlyRate=models.IntegerField('HourlyRate', null=False, blank=False, default=None)
    # DailyRate=models.IntegerField('DailyRate', null=False, blank=False, default=None)
    # WeeklyRate=models.IntegerField('WeeklyRate', null=False, blank=False, default=None)
    NumberOfBedrooms=models.IntegerField('Number of Bedrooms', null=True, blank=True, default=None)
    AreaOccupied=models.IntegerField('Area Of Property', null=True, blank=True, default=None)
    MonthlyRate=models.IntegerField('MonthlyRate', null=False, blank=False, default=None)
    # Owner=models.IntegerField('Listing Owner', blank=False, default=None)
    ListingImage=models.ImageField(null=False, blank=False, upload_to='images/', default=None)
    Contact=models.CharField('Listing Contact',null=False, blank=False, max_length=10, default=None)
    # ListingGallery=models.ImageField(null=True, blank=True, upload_to='images/')
    # Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    # Gallery=models.ForeignKey(ListingGallery2, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.Name


class GalleryImage(models.Model):
    Listing=models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True, default=None)
    Image=models.ImageField(null=True, blank=True, default=None, upload_to='images/')
    Name=models.CharField(null=True, blank=True, max_length=10, default=None)

    def __str__(self):
        return self.Name