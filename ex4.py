cars = 100
# number of cars 
space_in_a_car = 4
# number of space in a car
drivers = 30
# number of drivers
passengers = 90
# number of passengers
cars_not_driven = cars - drivers
# number of cars not driven
cars_driven = drivers
# the number of cars_driven is equal to the number of drivers
carpool_capacity = cars_driven * space_in_a_car
# capacity of carpool is equal to the cars_driven 
average_passengers_per_car = passengers / cars_driven
# number of passenger per car= passengers is divided by the number of cars driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."