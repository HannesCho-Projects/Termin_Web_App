from django.contrib import admin


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass
