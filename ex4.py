cars = 100
#100 cars
space_in_a_car = 4.0
#space in a car is 4
drivers = 30
#30 drivers
passengers = 90
#90 passengers
cars_not_driven = cars - drivers
#cars not driven is cars minus drivers
cars_driven = drivers
#cars driven is the number of drivers
carpool_capacity = cars_driven * space_in_a_car
#carpool capacity is cars driven times space in a car
average_passengers_per_car = passengers / cars_driven
#the average passegers per car is the number of passengers divided by cars driven


print("There are", cars, "cars available.")
#this will print stuff
print("There are only", drivers, "drivers available.")
#this will print stuff
print("There will be", cars_not_driven, "empty cars today.")
#this will print stuff
print("We can transport", carpool_capacity, "people today.")
#this will print stuff
print("We have", passengers, "to carpool today.")
#this will print stuff
print("We need to put about", average_passengers_per_car,
      "in each car.")
      #this will print stuff

#the variable is not defined, that's why there is the error
#it is fine
#ok
#commented
#