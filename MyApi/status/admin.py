from django.contrib import admin
from django.db.models.base import Model
from . models import Status

class StatusAdmin(admin.ModelAdmin):
      list_display=['user','content','image',]
      class Meta:
            model =Status


admin.site.register(Status, StatusAdmin)
