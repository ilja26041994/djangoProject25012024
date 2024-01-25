from django.db import models

# Create your models here.


class CarType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']


class CarBrand(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']


class Car(models.Model):
    car_number = models.CharField(max_length=255)
    car_type = models.CharField(CarType, on_delete=models.SET_NULL, null=True)
    car_brand = models.CharField(CarBrand, on_delete=models.SET_NULL, null=True)
    is_electric = models.BooleanField(default=False)
    year = models.IntegerField()


class Parking(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(null=True)


class ParkingSlot(models.Model):
    is_free = models.BooleanField(default=True)
    number = models.IntegerField()
    car = models.OneToOneField(Car, on_delete=models.SET_NULL, null=True)
    parking = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['number']
