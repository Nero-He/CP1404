from prac_08.taxi import Taxi

prius_car = Taxi('Prius 1', 100)
prius_car.drive(40)
print(prius_car.__str__())
print(prius_car.start_fare())

prius_car.drive(100)
print(prius_car.__str__())
print(prius_car.start_fare())

