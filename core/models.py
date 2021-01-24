from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.conf import settings
from embed_video.fields import EmbedVideoField

# Create your models here.
# about us model class
class AboutUs(models.Model):
    title         = models.CharField(max_length=150)
    content       = RichTextField()
    mission       = models.TextField()
    vision        = models.TextField()
    objectives    = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:200]

    class Meta:
        verbose_name_plural = "AboutUs"


# activities model class
class Activity(models.Model):
    video = EmbedVideoField()

    class Meta:
        verbose_name_plural = "Activities"


# bankInformation model class
class BankInformation(models.Model):
    bank_name           = models.CharField(max_length=150)
    branch              = models.CharField(max_length=150)
    account_number      = models.CharField(max_length=250)
    account_name        = models.CharField(max_length=250)

    def __str__(self):
        return self.account_name

    class Meta:
        verbose_name_plural = "BankInformations"


class Carasoul(models.Model):
    image      = models.ImageField(upload_to='pics/%Y/%m/%d/')
    title      = models.CharField(max_length=250)
    sub_title  = models.CharField(max_length=100,blank=True,null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Carasoul"


# our cause model class
class Cause(models.Model):
    image      = models.ImageField(upload_to='pics/%Y/%m/%d/')
    title      = models.CharField(max_length=150)
    timestamp    = models.DateTimeField(auto_now_add=True)
    content    = RichTextField()

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Causes"


# contact model class
class Contact(models.Model):
    icon      = models.ImageField(upload_to='pics/%Y/%m/%d/')
    title      = models.CharField(max_length=250)
    sub_title  = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Contacts"


# contact message class
class ContactMessage(models.Model):
    fullname      = models.CharField(max_length=100)
    email         = models.EmailField()
    subject       = models.CharField(max_length=250)
    message       = models.TextField()

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = "ContactMessages"


# donor model class
class Donor(models.Model):
    image     = models.ImageField(upload_to='pics/%Y/%m/%d/')
    name      = models.CharField(max_length=150)
    timestamp    = models.DateTimeField(auto_now_add=True)
    post      = models.CharField(max_length=150, verbose_name="Donors job ?")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Donors"


# bankForm model class
class Donation(models.Model):
    first_name        = models.CharField(max_length=200)
    last_name         = models.CharField(max_length=200)
    contact           = models.CharField(max_length=200)
    email             = models.EmailField()
    amount            = models.FloatField(max_length=200)
    transcition_id    = models.IntegerField()
    message           = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Donations"


# gallaries model class
class GalleryTitle(models.Model):
    title        = models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "GalleryTitles"

class Gallery(models.Model):
    gallery = models.ForeignKey(GalleryTitle, on_delete=models.CASCADE,null=True, blank=True)
    image      = models.ImageField(upload_to='pics/%Y/%m/%d/',null=True, blank=True)

    # def __str__(self):
    #     return self.id 
        
    class Meta:
        verbose_name_plural = "Gallaries"


# member model class
class Member(models.Model):
    image        = models.ImageField(upload_to='pics/%Y/%m/%d/')
    name         = models.CharField(max_length=150)
    post         = models.CharField(max_length=150)
    timestamp    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Members"


# program model class
class Program(models.Model):
    title     = models.CharField(max_length=100)
    slug      = models.SlugField()
    content   = RichTextField()
    image     = models.ImageField(upload_to='pics/%Y/%m/%d/')
    timestamp = models.DateTimeField(auto_now_add=True)
    featured  = models.BooleanField()

    class Meta:
        verbose_name_plural = "Programs"

    def timestamp_pretty(self):
        return self.timestamp.strftime('%b %e, %Y')

    def summary(self):
        return self.content[:70]

    def save(self, *args,**kwargs):
        original_slug = slugify(self.title)
        queryset      = Program.objects.all().filter(slug__iexact = original_slug).count()
        count         = 1
        slug          = original_slug

        while(queryset):
            slug     = original_slug + '-' + str(count)
            count   += 1
            queryset = Program.objects.all().filter(slug__iexact = slug).count()
        self.slug    = slug
        super(Program, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


    def get_absoulate_url(self):
        return reverse('core:details',kwargs ={
            'pk':self.pk
        })











