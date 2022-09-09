from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.house.count()
