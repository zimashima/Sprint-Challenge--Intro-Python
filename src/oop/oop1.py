# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#base class
class Vehicle:
    pass

#child class of parent class Vehicle
class GroundVehicle(Vehicle):
    pass

#child class of parent class Vehicle
class FlightVehicle(Vehicle):
    pass

#child class of parent class GroundVehicle
class Car(GroundVehicle):
    pass

#child class of parent class GroundVehicle
class Motorcycle(GroundVehicle):
    pass

#child class of parent class FlightVehicle
class Starship(FlightVehicle):
    pass

#child class of parent class FlightVehicle
class Airplane(FlightVehicle):
    pass
