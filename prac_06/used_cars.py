"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


class Limo:
    """Represent a Limo object."""

    def __init__(self, fuel=100):
        """Initialise a Car instance in 100 fuel.
        """
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self):
        """Add 20 to the Limo's fuel."""
        self.add_fuel(20)
        print('fuel =', self.fuel)

    def drive(self):
        Limo.drive(115)
        print("odo =", Limo.odometer)
        print(Limo)


main()
