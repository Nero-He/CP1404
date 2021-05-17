from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        number = random.uniform(0, 100)
        if number < self.reliability:
            distance_can_run = super().drive(distance)
        else:
            distance_can_run = super().drive(0)
        return distance_can_run
