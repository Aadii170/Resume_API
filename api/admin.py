from django.contrib import admin

# Register your models here.
from api.models import Resume
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'dob', 'profile', 'resume_file')
