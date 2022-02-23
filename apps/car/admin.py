from django.contrib import admin

from .models import Car, Rating


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "make",
        "model",
    )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        "car",
        "rating",
    )
