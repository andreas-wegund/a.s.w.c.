from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser





# from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register( CustomUser )
class CustomUserAdmin( admin.ModelAdmin ):
      list_display = [ 'email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active' ]
      list_filter = list_display
      ordering = [ 'email' ]
      search_fields = [ 'email', 'username', 'first_name', 'last_name' ]
      date_hierarchy = 'date_joined'
