from django.contrib.auth.models import User
from rest_framework import serializers

from flights_app.models import Flight, Order


#  flight = models.ForeignKey(Flight, on_delete=models.RESTRICT)
#     user = models.ForeignKey(User, on_delete=models.RESTRICT)
#     seats = models.IntegerField(db_column='num_seats', null=False, blank=False)
#     order_date = models.DateField(db_column='order_date', auto_now=True, null=False)
#     total_price


class OrderSerializer(serializers.ModelSerializer):

    flight_num = serializers.SerializerMethodField('get_flight_num')
    flight_origin = serializers.SerializerMethodField('get_flight_origin')
    flight_destin = serializers.SerializerMethodField('get_flight_destin')
    user_name = serializers.SerializerMethodField('get_user_name')

    class Meta:
        model = Order
        fields = ('flight', 'flight_num', 'flight_origin', 'flight_destin', 'user', 'user_name', 'seats', 'total_price')

    def get_flight_num(self, obj):
        flight = Flight.objects.get(pk=obj.flight.id)
        return flight.flight_number

    def get_flight_origin(self, obj):
        flight = Flight.objects.get(pk=obj.flight.id)
        return flight.origin_country

    def get_flight_destin(self, obj):
        flight = Flight.objects.get(pk=obj.flight.id)
        return flight.destination_country

    def get_user_name(self, obj):
        user = User.objects.get(pk=obj.user.id)
        return user.first_name + user.last_name


class UpdateOrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField('get_total_price')
    class Meta:
        model = Order
        fields = ('seats', 'flight', 'total_price')

    def get_total_price(self, obj):
        price_f = Flight.objects.get(pk=obj.flight.id).price
        seats_f = Order.objects.get(pk=obj.id).seats
        print(f"price: {price_f}, seats: {seats_f}")
        return round(price_f * seats_f, 2)

    # def update(self, instance, validated_data):
    #     # total_price = self.context['instance'].total_price
    #     total_price_f = instance.total_price
    #     validated_data['total_price'] = total_price_f
    #     return super().update(instance, validated_data)




