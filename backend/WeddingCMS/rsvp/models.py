from django.db import models


class Rsvp(models.Model):
    submission_date = models.DateTimeField('Submission date')
    invite_sent_date = models.DateTimeField('Invite sent date')


class MealChoice(models.Model):
    name = models.CharField(max_length=200)


class Attendee(models.Model):
    rsvp = models.OneToOneField(Rsvp, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    meal_choice = models.ForeignKey(MealChoice, on_delete=models.SET_NULL, blank=True, null=True)


class AttendeeGuest(models.Model):
    rsvp = models.ForeignKey(Rsvp, on_delete=models.CASCADE)
    guest_host = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    meal_choice = models.ForeignKey(MealChoice, on_delete=models.SET_NULL, blank=True, null=True)
