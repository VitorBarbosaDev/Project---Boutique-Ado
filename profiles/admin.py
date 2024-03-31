from django.contrib import admin
from .models import UserProfile  # Adjust the import path as necessary

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_country', 'default_town_or_city')
    search_fields = ('user__username', 'default_phone_number', 'default_town_or_city')
    readonly_fields = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
