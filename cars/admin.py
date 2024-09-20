from django.contrib import admin
from cars.models import Car, Brand


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "model",
        "brand",
        "price",
        "factory_year",
        "model_year",
        "creation_date_time",
        "modified_date_time",
    ]
    search_fields = [
        "model",
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
