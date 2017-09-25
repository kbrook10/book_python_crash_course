# (1) - Loop through list and upper case bmw

cars = []

cars.append("audi")
cars.append("bmw")
cars.append("subaru")
cars.append("toyota")

print(cars)

for car in cars:
	if car == "bmw":
	    print(car.upper())
	else:
		print(car.title())

print("Finished Loop")

# (2) Testing for equality using conditionals

car = 'bmw'
print(car == 'bmw')

