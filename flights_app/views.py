from django.shortcuts import render
from rest_framework import mixins, viewsets

from flights_app.models import Flight
from flights_app.serializers import FlightSerializer


# Create your views here.


class FlightsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


def sign_up():
    pass