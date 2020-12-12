from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers, viewsets

from rsvp.models import Rsvp, Attendee, AttendeeGuest


class AttendeeGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendeeGuest
        fields = '__all__'


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'


class RSVPSerializer(WritableNestedModelSerializer):
    attendee = AttendeeSerializer()
    attendee_guest = AttendeeGuestSerializer(allow_null=True, many=True)

    class Meta:
        model = Rsvp
        fields = '__all__'


class RSVPViewSet(viewsets.ModelViewSet):
    queryset = Rsvp.objects.all()
    serializer_class = RSVPSerializer
