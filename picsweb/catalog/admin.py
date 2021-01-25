from django.contrib import admin
from .models import User, Profile, Upload

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
 ... 

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
 ... 
 
@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
 ... 