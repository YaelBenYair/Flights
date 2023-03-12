from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Flight(models.Model):

    flight_number = models.CharField(db_column='flight_number', max_length=256, null=False, blank=False)
    origin_country = models.CharField(db_column='origin_country', max_length=256, null=False, blank=False)
    origin_city = models.CharField(db_column='origin_city', max_length=256, null=False, blank=False)
    origin_airport_code = models.CharField(db_column='origin_airport_code', max_length=256, null=False, blank=False)
    destination_country = models.CharField(db_column='destination_country', max_length=256, null=False, blank=False)
    destination_city = models.CharField(db_column='destination_city', max_length=256, null=False, blank=False)
    destination_airport_code = models.CharField(db_column='destination_airport_code', max_length=256, null=False,
                                                blank=False)
    origin_datetime = models.DateTimeField(db_column='origin_datetime', null=False, blank=False)
    destination_datetime = models.DateTimeField(db_column='destination_datetime', null=False, blank=False)
    total_seats = models.IntegerField(db_column='total_seats', null=False, blank=False,
                                      validators=[MinValueValidator(0)])
    seats_left = models.IntegerField(db_column='seats_left', null=False, blank=False, validators=[MinValueValidator(0)])
    is_cancelled = models.BooleanField(db_column='is_cancelled', null=False, blank=False)
    price = models.FloatField(db_column='price', null=False, blank=False)

    class Meta:
        db_table = 'flights'


class Order(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    seats = models.IntegerField(db_column='num_seats', null=False, blank=False)
    order_date = models.DateField(db_column='order_date', auto_now=True, null=False)
    total_price = models.FloatField(db_column='total_price')

    def clean(self):
        if self.seats > self.flight.seats_left:
            raise ValidationError(f'The number of ordered seats cannot exceed the available seats on the flight. '
                                  f'Only {self.flight.seats_left} places left')

    # def clean(self):
    #     if self.seats > self.flight.seats_left:
    #         raise ValidationError({
    #             'seats': 'Number of ordered seats cannot exceed available seats of the flight.'
    #         })

    def save(self, *args, **kwargs):
        # self.full_clean()  # validate the Order object
        self.total_price = self.seats * self.flight.price
        super().save(*args, **kwargs)  # save the Order object

        # update the Flight object with the new seats_left value
        self.flight.seats_left -= self.seats
        self.flight.save(update_fields=['seats_left'])

        # Order.save(update_fields=['total_price'])


    class Meta:
        db_table = 'orders'














