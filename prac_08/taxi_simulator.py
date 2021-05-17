from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive !")
    option_menu = input("(q)uit, (c)hoose taxi, (d)rive").lower()
    car_prius = Taxi('Prius', 100)
    car_limo = SilverServiceTaxi('Limo', 100, 2)
    car_hummer = SilverServiceTaxi('Hummer', 200, 4)
    cars = [car_prius, car_limo, car_hummer]
    taxi_choose = ""
    while option_menu != 'q':
        if option_menu == 'c':
            taxi_choose = choose_car(cars)
        elif option_menu == 'd':
            bill_to_date = drive(cars, taxi_choose, bill_to_date)
        else:
            print('Invalid option')
        print('Bill to date: $ {}'.format(bill_to_date))
        option_menu = input("(q)uit, (c)hoose taxi, (d)rive").lower()
    print("Total trip cost: ${}".format(bill_to_date))
    print("Taxis are now:")


# for the optional of cars
def choose_car(cars):
    car_list = []
    print('Taxis available:')
    for i, each in enumerate(cars):
        car_list.append(i)
        print(f"{i} - {each.__str__()}")
    taxi_choose = input("Choose taxi:")
    taxi_choose = int(taxi_choose)
    if taxi_choose in car_list:
        taxi_choose = taxi_choose
    else:
        print('Invalid taxi choice')
        taxi_choose = ""
    return taxi_choose


# For calculation of the bill
def drive(cars, taxi_choose, bill_to_date):
    if taxi_choose == '':
        bill_to_date = 0
        return bill_to_date
    else:
        cars[taxi_choose].start_fare()
        distance = int(input('Drive how far? '))
        cars[taxi_choose].drive(distance)
        print(f"Your {cars[taxi_choose].name} trip cost you ${cars[taxi_choose].get_fare()}")
        bill_to_date += cars[taxi_choose].get_fare()
    return bill_to_date


main()
