from prac_06.guitar import Guitar


def main():
    test1 = Guitar('Gibson L-5 CES', 1922, 6200)
    test2 = Guitar('Another Guitar', 2013, 6200)
    test3 = Guitar('50-year- old guitar', 1970, 6200)
    print(f'Gibson L-5 CES get_age() - Expected 98. Got {test1.get_age()}')
    print(f"Another Guitar get_age() - Expected 8. Got {test2.get_age()}")
    print(f"Another Guitar get_age() - Expected True. Got {test2.is_vintage()}")
    print(f'50-year- old guitar get_age() - Expected True. Got {test3.is_vintage()}')


main()
