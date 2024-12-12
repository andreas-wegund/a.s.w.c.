from django.contrib import admin

from features.models import Feature





# Register your models here.
@admin.register( Feature )
class FeatureAdmin( admin.ModelAdmin ):
      list_display = [ 'feature_name', 'developer', 'staging_enabled', 'production_enabled', 'created' ]
      search_fields = list_display
      date_hierarchy = 'created'
