from django.contrib import admin

from .models import Rsvp, Attendee, AttendeeGuest, MealChoice


# class AttendeeInline(admin.StackedInline):
#     classes = ['collapse']
#     model = Attendee
#
#
class AttendeeGuestInline(admin.StackedInline):
    classes = ['collapse']
    fields = ['first_name', 'last_name', 'meal_choice']
    model = AttendeeGuest
    extra = 3


class RsvpAdmin(admin.ModelAdmin):
    # inlines = [AttendeeInline, AttendeeGuestInline]
    inlines = [AttendeeGuestInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            if formset.model == AttendeeGuest:
                instance.guest_host = form.instance.attendee

            instance.save()
        formset.save_m2m()


admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Attendee)
admin.site.register(AttendeeGuest)
admin.site.register(MealChoice)
