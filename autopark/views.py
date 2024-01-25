from django.http import HttpResponse
from django.shortcuts import render
from .models import Car, CarBrand, CarType, Parking, ParkingSlot
# Create your views here.

def initialaze(request):
    try:
        car_types = [
            CarType(name="Sedan"),
            CarType(name="Hatchback"),
            CarType(name="SUV"),
            CarType(name="Pickup"),
            CarType(name="Coupe"),
            CarType(name="Convertible"),
            CarType(name="Van"),
            CarType(name="Wagon"),
            CarType(name="Truck"),
            CarType(name="Bus"),
            CarType(name="Trailer"),
            CarType(name="Motorcycle"),
            CarType(name="Scooter"),
            CarType(name="Electric"),
        ]

        car_brands = [
            CarBrand(name="Toyota"),
            CarBrand(name="Nissan"),
            CarBrand(name="Honda"),
            CarBrand(name="Ford"),
            CarBrand(name="Chevrolet"),
            CarBrand(name="Volkswagen"),
            CarBrand(name="BMW"),
            CarBrand(name="Mercedes"),
            CarBrand(name="Audi"),
            CarBrand(name="Hyundai"),
            CarBrand(name="Kia"),
            CarBrand(name="Mazda"),
            CarBrand(name="Subaru"),
            CarBrand(name="Suzuki"),
            CarBrand(name="Jeep"),
            CarBrand(name="Dodge"),
            CarBrand(name="Ram"),
            CarBrand(name="Buick"),
            CarBrand(name="GMC"),
            CarBrand(name="Lincoln"),
            CarBrand(name="Cadillac"),
            CarBrand(name="Chrysler"),
            CarBrand(name="Infiniti"),
            CarBrand(name="Jaguar"),
            CarBrand(name="Land Rover"),
            CarBrand(name="Aston Martin"),
            CarBrand(name="Lexus"),
            CarBrand(name="MINI"),
            CarBrand(name="Tesla"),
            CarBrand(name="Ferrari"),
            CarBrand(name="Lotus"),
            CarBrand(name="Fiat"),
            CarBrand(name="Mitsubishi"),
        ]


        parks= [
            Parking(name="park1", address="address1", phone_number="123456789", price=100),
            Parking(name="park2", address="address2", phone_number="123456789", price=200),
        ]

        park_slots_1 = [
            ParkingSlot(is_free=True, number=1),
            ParkingSlot(is_free=True, number=2),
            ParkingSlot(is_free=True, number=3),
            ParkingSlot(is_free=True, number=4),
            ParkingSlot(is_free=True, number=5),
            ParkingSlot(is_free=True, number=6),
            ParkingSlot(is_free=True, number=7),
            ParkingSlot(is_free=True, number=8),
            ParkingSlot(is_free=True, number=9),
            ParkingSlot(is_free=True, number=10),
        ]

        park_slots_2 = [
            ParkingSlot(is_free=True, number=1),
            ParkingSlot(is_free=True, number=2),
            ParkingSlot(is_free=True, number=3),
            ParkingSlot(is_free=True, number=4),
            ParkingSlot(is_free=True, number=5),
            ParkingSlot(is_free=True, number=6),
            ParkingSlot(is_free=True, number=7),
            ParkingSlot(is_free=True, number=8),
            ParkingSlot(is_free=True, number=9),
            ParkingSlot(is_free=True, number=10),
        ]

        cars = [
            Car(car_number="123456", car_type=CarType.objects.get(name="Sedan"), car_brand=CarBrand.objects.get(name="Audi"), is_electric=False, year=2020),
            Car(car_number="123456", car_type=CarType.objects.get(name="Sedan"), car_brand=CarBrand.objects.get(name="volkswagen"), is_electric=False, year=2021),
            Car(car_number="123456", car_type=CarType.objects.get(name="Sedan"), car_brand=CarBrand.objects.get(name="BMW"), is_electric=False, year=2022),
            Car(car_number="123456", car_type=CarType.objects.get(name="Sedan"), car_brand=CarBrand.objects.get(name="Mercedes"), is_electric=False, year=2023),
        ]

        for car_type in car_types:
            car_type.save()
        for car_brand in car_brands:
            car_brand.save()
        for park in parks:
            park.save()
        for park_slot_1 in park_slots_1:
            park_slot_1.save()
        for park_slot_2 in park_slots_2:
            park_slot_2.save()
        for car in cars:
            car.save()

        return HttpResponse("Success")

    except:
        return HttpResponse('Error')