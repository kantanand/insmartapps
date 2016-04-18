from __future__ import unicode_literals

import os
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from datacenter.storage import OverwriteStorage

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

def profile_picture_name(instance, filename):
    return '/'.join(['content', str(instance.user.id), "profile_picture.jpg"])

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    father_name  = models.CharField(max_length=50, blank=True)
    mother_name  = models.CharField(max_length=50, blank=True)
    primary_email = models.CharField(max_length=250)
    secondary_email = models.CharField(max_length=250, blank=True)
    primary_mobile      = models.CharField(max_length=20)
    secondary_mobile = models.CharField(max_length=20, blank=True)
    landline   = models.CharField(max_length=15, blank=True)
    door_no     = models.CharField(max_length=10, blank=True)
    street_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    locality = models.CharField(max_length=50, blank=True)
    city        = models.CharField(max_length=50, blank=True)
    state       = models.CharField(max_length=50, blank=True)
    country     = models.CharField(max_length=50, blank=True)
    pincode     = models.CharField(max_length=15, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    blood_group = models.CharField(max_length=10, blank=True)
    picture         = models.ImageField(upload_to=profile_picture_name, storage=OverwriteStorage(), blank=True)
    source_media    = models.CharField(max_length=250, blank=True)
    facebook_media  = models.CharField(max_length=250, blank=True)
    google_media    = models.CharField(max_length=250, blank=True)
    linkedin_media  = models.CharField(max_length=250, blank=True)
    twitter_media   = models.CharField(max_length=250, blank=True)
    # Record Tracking
    created_by = models.CharField(max_length=250, blank=True)
    created_date    = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now = True, blank=True, null=True)
    # Education Details ==============================
    qualification = models.CharField(max_length=100, blank=True)
    school_college_name = models.CharField(max_length=100, blank=True)
    year_passout = models.CharField(max_length=4, blank=True)
    # User Roles
    is_admin     = models.BooleanField(default=0)
    is_teacher   = models.BooleanField(default=0)
    is_member    = models.BooleanField(default=0)
    # website = models.URLField(blank=True)

    class Meta:
        app_label = 'datacenter'
        managed = True

    # override the unicode method to return the username on this model
    def __unicode__(self):
        return self.user.username

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance,email=instance.username)
    post_save.connect(create_user_profile, sender=User)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
