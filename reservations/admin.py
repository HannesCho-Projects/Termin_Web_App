from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    list_display = (
        "house",
        "status",
        "check_in",
        "check_out",
        "guest",
        "is_finished",
    )

    list_filter = ("status",)
