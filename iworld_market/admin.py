from django.contrib import admin
from .models import Course, Offer


class Iworld_marketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seat_available')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Course, Iworld_marketAdmin)
admin.site.register(Offer, OfferAdmin)

