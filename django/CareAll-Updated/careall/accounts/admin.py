from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User,CareSeeker,CareGiver

admin.site.register(User,UserAdmin)
admin.site.register(CareSeeker)
admin.site.register(CareGiver)

