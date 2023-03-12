from datetime import datetime, time

from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from flights_app.models import Flight
from flights_app.serializers.flight import FlightSerializer


class FlightsPaginationClass(PageNumberPagination):
    page_size = 10


class FlightsPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PATCH', 'PUT', 'POST']:
            return request.user.is_authenticated and request.user.is_staff
        return True


# ModelViewSet
class FlightsViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):

    queryset = Flight.objects.all()
    permission_classes = [FlightsPermissions]
    serializer_class = FlightSerializer

    # arrival and departure dates range
    def get_queryset(self):
        qs = self.queryset

        # filter queryset - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#id4
        if self.action == 'list':
            if 'flight_number' in self.request.query_params:
                qs = qs.filter(flight_number__icontains=self.request.query_params['flight_number'])
            if 'origin' in self.request.query_params:
                qs = qs.filter(origin_country__icontains=self.request.query_params['origin'])
            if 'destination' in self.request.query_params:
                qs = qs.filter(destination_country__icontains=self.request.query_params['destination'])
            if 'price_start' in self.request.query_params:
                qs = qs.filter(price__gte=self.request.query_params['price_start'])
            if 'price_end' in self.request.query_params:
                qs = qs.filter(price__lte=self.request.query_params['price_end'])
            if 'is_canceled' in self.request.query_params:
                qs = qs.filter(is_cancelled=self.request.query_params['is_canceled'].title())
            if 'arrival_date_st' in self.request.query_params and \
                    'arrival_date_nd' in self.request.query_params:
                # '%d-%m-%Y'
                date_time_obj = datetime.strptime(self.request.query_params['arrival_date_st'], '%Y-%m-%d')
                date_time_obj2 = datetime.strptime(self.request.query_params['arrival_date_nd'], '%Y-%m-%d')
                # start_date = datetime.combine(date_time_obj, time())
                # end_date = datetime.combine(date_time_obj2, time())
                start_date = datetime.date(date_time_obj)
                end_date = datetime.date(date_time_obj2)
                qs = qs.filter(origin_datetime__range=(start_date, end_date))

            if 'departure_date_st' in self.request.query_params and \
                    'departure_date_nd' in self.request.query_params:
                date_time_obj = datetime.strptime(self.request.query_params['departure_date_st'], '%Y-%m-%d')
                date_time_obj2 = datetime.strptime(self.request.query_params['departure_date_nd'], '%Y-%m-%d')
                start_date = datetime.date(date_time_obj)
                end_date = datetime.date(date_time_obj2)
                qs = qs.filter(destination_datetime__range=(start_date, end_date))
        return qs
