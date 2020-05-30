from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User,CareSeeker,CareGiver

from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        *BaseUserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'age','gender','image','address','contact','slug'
                ),
            },
        ),
    )






admin.site.register(User,UserAdmin)
admin.site.register(CareSeeker)
admin.site.register(CareGiver)

