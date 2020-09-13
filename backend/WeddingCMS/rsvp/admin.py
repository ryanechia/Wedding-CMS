from django.contrib import admin

from .models import Rsvp, Attendee, AttendeeGuest, MealChoice


class AttendeeInline(admin.StackedInline):
    classes = ['collapse']
    model = Attendee


class AttendeeGuestInline(admin.StackedInline):
    classes = ['collapse']
    model = AttendeeGuest
    extra = 3


class RsvpAdmin(admin.ModelAdmin):
    inlines = [AttendeeInline, AttendeeGuestInline]


admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Attendee)
admin.site.register(AttendeeGuest)
admin.site.register(MealChoice)
