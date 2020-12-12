from django.db import models


class MealChoice(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Attendee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    meal_choice = models.ForeignKey(MealChoice, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Rsvp(models.Model):
    submission_date = models.DateTimeField('Submission date')
    invite_sent_date = models.DateTimeField('Invite sent date')
    attendee = models.OneToOneField(Attendee, on_delete=models.CASCADE)

    def __str__(self):
        return self.attendee.first_name + ' ' + self.attendee.last_name


class AttendeeGuest(models.Model):
    rsvp = models.ForeignKey(Rsvp, on_delete=models.CASCADE)
    guest_host = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    meal_choice = models.ForeignKey(MealChoice, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
