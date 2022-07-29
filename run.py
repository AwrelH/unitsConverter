# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def retry_message():
    print('\nWish to test out some other values?')
    print('(Y)es or (N)o?')   


def degrees():
    """
    Function to convert celcius to fahrenheit and vice versa.
    """
    print('You have choosen the degrees option')
    print('What do you wish to convert? 1.Fahrenheit or 2.Celcius?')
    option = input('enter you option(1 or 2): ')
    if option == '1':
        print('Fahrenheit it is...')
        option_value = input('\nWrite down a temperature: ')
        if not option_value.isdigit():
            print('invalid input, try again')
            degrees()
        else:
            cel_value = round((int(option_value)-32) * 5 / 9, 2)
            print(f'\t{option_value} F equals {cel_value} deg. Celcius')
            retry_message()
            retry_answer = input()
            if retry_answer == 'y':
                degrees()
            else:
                welcome()
    elif option == '2':
        print('Celcius it is...')
        option_value = input('\nWrite down a temperature: ')
        if not option_value.isdigit():
            print('invalid input, try again')
            degrees()
        else:
            fahr_value = round((int(option_value)*1.8) + 32, 2)
            print(f'\t{option_value} C equals {fahr_value} deg. Fahrenheit\n')
            retry_message()
            retry_answer = input()
            if retry_answer == 'y':
                degrees()
            else: 
                welcome()

    else:
        validate_opt(option)
        degrees()


def meters():
    """
    This function will convert meters to feet and vice versa.
    """
    print('You have choosen the meters option')
    print('What do you wish to convert? 1.Feet or 2.Meters?')
    option = input('enter you option(1 or 2): ')
    if option == '1':
        print('Feet it is...')
        option_value = input('\nHow many feet: ')
        if not option_value.isdigit():
            print('invalid input, try again')
            meters()
        else:
            meter_value = round(float(option_value) / 3.2808399, 2)
            print(f'\t{option_value} feet equals {meter_value} meters')
            retry_message()
            retry_answer = input()
            if retry_answer == 'y':
                meters()
            else:
                welcome()
    elif option == '2':
        print('meters it is...')
        option_value = input('\nHow many meters: ')
        if not option_value.isdigit():
            print('invalid input, try again')
            meters()
        else:
            feet_value = round(float(option_value) * 3.2808399, 2)
            print(f'\t{option_value} meter(s) equals {feet_value} feet')
            retry_message()
            retry_answer = input()
            if retry_answer == 'y':
                meters()
            else:
                welcome()
    else:
        validate_opt(option)
        meters()


def kilos():
    """
    This function will convert kilos to pounds and vice versa.
    """
    print('You have choosen the kilos option')
    print('What do you wish to convert? 1.Kilos or 2.Pounds?')
    option = input('enter you option(1 or 2): ')
    if option == '1':
        print('Kilos it is...')
        option_value = input('\nHow many kilos: ')
        if not option_value.isdigit():
            print('invalid input, try again')
            kilos()
        else:
            pounds_value = round(float(option_value) * 2.20462262, 2)
            print(f'\t{option_value} kilo(s) equals {pounds_value} pound(s)')
            retry_message()
            retry_answer = input()
            if retry_answer == 'y':
                kilos()
            else:
                welcome()
    elif option == '2':
        print('Pounds it is...')
        option_value = input('\nHow many pounds: ')
        if not option_value.isdigit():
            print('invalid input, try again')
            kilos()
        else:
            kilos_value = round(float(option_value) / 2.20462262, 2)
            print(f'\t{option_value} pound(s) equals {kilos_value} kilo(s)')
            retry_message()
            retry_answer = input()
            if retry_answer == 'y':
                kilos()
            else:
                welcome()

    else:
        validate_opt(option)
        kilos()


def liters():
    """
    This function will convert liters to gallons and vice versa.
    """
    print('You have choosen the liters option')
    print('What do you wish to convert? 1.Liters or 2.Gallons?')
    option = input('enter you option(1 or 2): ')
    if option == '1':
        print('Liters it is...')
        option_value = input('\nHow many liters: ')
        if not option_value.isdigit():
            print('invalid input, try again')
            liters()
        else:
            gallons_value = round(int(option_value) / 3.78541178, 2)
            print(f'\t{option_value} liter(s) equals {gallons_value} gallon(s)')
            retry_message()
            retry_answer = input()
            if retry_answer == 'y':
                degrees()
            else:
                welcome()     
    elif option == '2':
        print('Gallons it is...')
        option_value = input('\nHow many gallons: ')
        if not option_value.isdigit():
            print('invalid input, try again')
            liters()
        else:
            liters_value = round(int(option_value) * 3.78541178, 2)
            print(f'\t{option_value} gallon(s) equals {liters_value} liter(s)')
            retry_message()
            retry_answer = input()
            if retry_answer == 'y':
                degrees()
            else:
                welcome()     
    else:
        validate_opt(option)
        degrees()



def welcome():
    """
    Print welcome message
    """
    message = """welcome to the unit converter!\n
        Units you can convert:\n
        1 = celcius/fahrenheit\n
        2 = meters/feet\n
        3 = kilogram/pound\n
        4 = liters/us gallons\n
        5 = for exit the program
        make your choice my entering one of the above(1-4) options.
        """
    print(message)
    while True:
        choice = input()
        if validate(choice):
            if choice == '1':
                degrees()
            elif choice == '2':
                meters()
            elif choice == '3':
                kilos()
            elif choice == '4':
                liters()
            elif choice == '5':
                print('Thank you for testing the program!')
                return
        else:
            welcome()
        return True


def validate(values):
    """
    Inside try, raise error, if input not equal to,
    1,2,3,4,5.
    """
    try:
        (values)
        if values not in ('1', '2', '3', '4', '5'):
            raise ValueError(f"1,2,3,4 are valid values, you typed {values}")
    except ValueError as e:
        print(f"Invalid input: {e}, try again.\n")
        return False
    return True


def validate_opt(values):
    try:
        if values not in ("1", "2"):
            raise ValueError(f"1,2 are valid values, you typed {values}")
    except ValueError as e:
        print(f"Invalid input: {e}, try again.\n")
        return False
    return True

        


welcome()

