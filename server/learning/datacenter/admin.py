from django.contrib import admin

from .models import UserProfile, CourseMaster, SubjectMaster, ChapterMaster, QuestionBankMaster
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CourseMaster)
admin.site.register(SubjectMaster)
admin.site.register(ChapterMaster)
admin.site.register(QuestionBankMaster)




