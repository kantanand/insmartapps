# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datacenter.storage
from django.conf import settings
import datacenter.models.learning_course


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datacenter', '0002_auto_20160508_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter_name', models.CharField(max_length=250)),
                ('chapter_description', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=250)),
                ('course_description', models.TextField(blank=True)),
                ('course_duration', models.IntegerField(default=0, blank=True)),
                ('course_fee', models.IntegerField(default=0)),
                ('course_icon', models.ImageField(storage=datacenter.storage.OverwriteStorage(), upload_to=datacenter.models.learning_course.course_icon_folder, blank=True)),
                ('course_access', models.CharField(blank=True, max_length=50, choices=[('Public', 'Public'), ('Private', 'Private')])),
                ('course_type', models.CharField(blank=True, max_length=50, choices=[('K12', 'K12'), ('Regular', 'Regular')])),
                ('is_published', models.BooleanField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='QuestionBankMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_name', models.TextField(blank=True)),
                ('option_value_1', models.TextField(blank=True)),
                ('option_value_2', models.TextField(blank=True)),
                ('option_value_3', models.TextField(blank=True)),
                ('option_value_4', models.TextField(blank=True)),
                ('correct_option', models.CharField(blank=True, max_length=50, choices=[('option_value_1', 'option 1'), ('option_value_2', 'option 2'), ('option_value_3', 'option 3'), ('option_value_4', 'option 4')])),
                ('is_published', models.BooleanField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('chapter_name', models.ForeignKey(to='datacenter.ChapterMaster', blank=True)),
                ('course_name', models.ForeignKey(to='datacenter.CourseMaster', blank=True)),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubjectMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=250)),
                ('subject_description', models.TextField(blank=True)),
                ('subject_icon', models.ImageField(storage=datacenter.storage.OverwriteStorage(), upload_to=datacenter.models.learning_course.subject_icon_folder, blank=True)),
                ('is_published', models.BooleanField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='questionbankmaster',
            name='subject_name',
            field=models.ForeignKey(to='datacenter.SubjectMaster', blank=True),
        ),
    ]
