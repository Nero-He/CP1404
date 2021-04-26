email = {}
while True:
    user_email = input('Please type in your email address: ')
    if user_email == '':
        email[user_email] = name
        print(name, email[user_email])
        break
    name = input('Enter your name: ')
    while user_email in email:
        if user_email in email:
            option = input('Is your name {}? (Y/N)'.format(name)).upper()
            if option != '' or 'Y':
                new_name = input('Name: ')
                email[user_email] = new_name
                break
        else:
            break
