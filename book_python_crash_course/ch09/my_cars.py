# (1) Import Classes to create two separate types of cars

# from car import Car, ElectricCar
# import electric_car
# import car
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
my_tesla = ElectricCar('tesla', 'roadster', 2016)

cars = [my_beetle, my_tesla]

for car in cars:
	print(car.get_descriptive_name())