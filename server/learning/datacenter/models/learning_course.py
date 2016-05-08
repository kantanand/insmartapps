from __future__ import unicode_literals

import os
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from datacenter.storage import OverwriteStorage

# Course Master
def course_icon_folder(instance, filename):
    return '/'.join(['content', str(instance.course_name), "course_icon.jpg"])

class CourseMaster(models.Model):
    COURSE_ACCESS = (
        ('Public','Public'),
        ('Private','Private'),
    )

    COURSE_TYPE = (
        ('K12','K12'),
        ('Regular','Regular'),
    )

    course_name = models.CharField(max_length=250)
    course_description = models.TextField(blank=True)
    course_duration = models.IntegerField(blank=True, default=0)
    course_fee = models.IntegerField(default=0)
    course_icon = models.ImageField(upload_to=course_icon_folder, storage=OverwriteStorage(), blank=True)
    course_access = models.CharField(max_length=50, choices=COURSE_ACCESS, blank=True)
    course_type = models.CharField(max_length=50, choices=COURSE_TYPE, blank=True)
    is_published    = models.BooleanField(default=0)
    # Record Tracking
    created_by      = models.ForeignKey(User, blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now = True, blank=True, null=True)
    # website = models.URLField(blank=True)

    class Meta:
        app_label = 'datacenter'
        managed = True

    # override the unicode method to return the course_name on this model
    def __unicode__(self):
        return self.course_name

# Subject Master
def subject_icon_folder(instance, filename):
    return '/'.join(['content', str(instance.subject_name), "subject_icon.jpg"])

class SubjectMaster(models.Model):
    subject_name = models.CharField(max_length=250)
    subject_description = models.TextField(blank=True)
    subject_icon = models.ImageField(upload_to=subject_icon_folder, storage=OverwriteStorage(), blank=True)
    is_published    = models.BooleanField(default=0)
    # Record Tracking
    created_by      = models.ForeignKey(User, blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now = True, blank=True, null=True)
    # website = models.URLField(blank=True)

    class Meta:
        app_label = 'datacenter'
        managed = True

    # override the unicode method to return the subject_name on this model
    def __unicode__(self):
        return self.subject_name

# Chapter Master
class ChapterMaster(models.Model):
    chapter_name = models.CharField(max_length=250)
    chapter_description = models.TextField(blank=True)
    is_published    = models.BooleanField(default=0)
    # Record Tracking
    created_by      = models.ForeignKey(User, blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now = True, blank=True, null=True)
    # website = models.URLField(blank=True)

    class Meta:
        app_label = 'datacenter'
        managed = True

    # override the unicode method to return the chapter_name on this model
    def __unicode__(self):
        return self.chapter_name

# Question Bank Master
class QuestionBankMaster(models.Model):
    ANSWER_OPTION = (
        ('option_value_1','option 1'),
        ('option_value_2','option 2'),
        ('option_value_3','option 3'),
        ('option_value_4','option 4'),
    )

    course_name = models.ForeignKey(CourseMaster, blank=True)
    subject_name = models.ForeignKey(SubjectMaster, blank=True)
    chapter_name = models.ForeignKey(ChapterMaster, blank=True)
    question_name = models.TextField(blank=True)
    option_value_1 = models.TextField(blank=True)
    option_value_2 = models.TextField(blank=True)
    option_value_3 = models.TextField(blank=True)
    option_value_4 = models.TextField(blank=True)
    correct_option = models.CharField(max_length=50, choices=ANSWER_OPTION, blank=True)
    is_published    = models.BooleanField(default=0)
    # Record Tracking
    created_by      = models.ForeignKey(User, blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now = True, blank=True, null=True)
    # website = models.URLField(blank=True)

    class Meta:
        app_label = 'datacenter'
        managed = True

    # override the unicode method to return the question_name on this model
    def __unicode__(self):
        return self.question_name