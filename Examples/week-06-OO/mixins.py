import time

class LoggingMixin(object):
    def log(self):
        print "%s: %s" % (time.time(), self.__repr__())

class Vehicle(object):
    def log(self):
        print self.__repr__()

class TwoWheeledVehicle(Vehicle):
    pass

class LightVehicle(Vehicle):
    pass

class HeavyVehicle(Vehicle):
    pass

class Bike(TwoWheeledVehicle, LightVehicle):
    pass

class MotorCycle(TwoWheeledVehicle, HeavyVehicle):
    pass

class Tank(HeavyVehicle):
    pass

bike = Bike()
tank = Tank()

bike.log()
tank.log()
