from django.contrib import admin
from userprofile.models import User,Reviews
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Reviews)
