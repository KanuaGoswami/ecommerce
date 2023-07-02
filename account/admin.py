from django.contrib import admin
from .models import customUser
# Register your models here.
@admin.register(customUser)
class customUserAdmin(admin.ModelAdmin):
    fields=['phone','address','username','email','password','image','role','gst']