from rest_framework import serializers, viewsets
from rsvp.models import Rsvp


class RSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rsvp
        fields = '__all__'


class RSVPViewSet(viewsets.ModelViewSet):
    queryset = Rsvp.objects.all()
    serializer_class = RSVPSerializer
