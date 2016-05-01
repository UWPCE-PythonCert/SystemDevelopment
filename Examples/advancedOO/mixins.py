import time


class Base(object):
    def log(self):
        pass


class LoggingMixin(Base):
    def log(self):
        print("%s" % time.time(),)
        print("self is:", self)
        super(LoggingMixin, self).log()


class Vehicle(Base):
    def log(self):
        print(self.__repr__())
        super(Vehicle, self).log()


class TwoWheeledVehicle(Vehicle):
    pass


class LightVehicle(Vehicle):
    pass


class HeavyVehicle(Vehicle):
    pass


class Bike(LoggingMixin, TwoWheeledVehicle, LightVehicle):
    pass


class MotorCycle(TwoWheeledVehicle, HeavyVehicle):
    pass


class Tank(HeavyVehicle):
    pass


bike = Bike()
tank = Tank()

bike.log()
tank.log()
