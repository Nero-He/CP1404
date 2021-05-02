from prac_06.guitar import Guitar


def main():
    group_guitar = []
    print('My guitars!')
    end = 'False'
    while end != '':
        name = input('Name: ')
        year = input('Year: ')
        cost = input('Cost: ')
        group_guitar.append(Guitar(name, year, cost))
        print('{} ({}): ${} added.'.format(name, year, cost))
        end = input('')

    print('These are my guitars: ')
    for i, guitar in enumerate(group_guitar):
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost))


main()
