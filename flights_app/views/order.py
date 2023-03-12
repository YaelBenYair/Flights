from rest_framework import mixins, status, serializers
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from flights_app.models import Order, Flight
from flights_app.serializers.order import OrderSerializer, UpdateOrderSerializer


class OrderPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST']:
            flight_id = request.data.get('flight')
            if Flight.objects.get(pk=flight_id).is_cancelled:
                raise serializers.ValidationError({"detail": "Cannot create order for cancelled flight."})
            else:
                return request.user.is_authenticated

        if request.method in ['GET']:
            if not(request.parser_context['kwargs'].get('pk')):
                return request.user.is_authenticated and request.user.is_staff

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'PUT']:
            return request.user.is_authenticated and request.user.id == obj.user_id

        if request.method in ['GET']:
            if request.parser_context['kwargs'].get('pk'):
                return request.user.is_authenticated and request.user.id == obj.user_id

        return True


class OrderViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):

    queryset = Order.objects.all()
    permission_classes = [OrderPermissions]
    # serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'list', 'retrieve']:
            return OrderSerializer
        if self.request.method in ['PATCH', 'PUT']:
            return UpdateOrderSerializer

    def create(self, request, *args, **kwargs):
        data_copy = request.data.copy()
        data_copy['user'] = request.user.id
        data_copy['total_price'] = int(request.data['seats']) * Flight.objects.get(pk=request.data['flight']).price
        # data_copy['total_price'] = 1166.85
        print(data_copy)
        serializer = self.get_serializer(data=data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
















