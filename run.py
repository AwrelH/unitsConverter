# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
            print(f'invalid input, try again')
            degrees()
        else:
            cel_value = round((int(option_value)-32) * 5 / 9, 2)
            print(f'{option_value} F equals {cel_value} degrees Celcius')


    elif option == '2':
        print('Celcius it is...')
        option_value = input('\nWrite down a temperature: ')

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
        make your choice my entering one of the above(1-4) options.
        """
    print(message)
    while True:
        choice = input()
        if validate(choice):
            if choice == '1':
                degrees()
            elif choice == '2':
                print('2 = meters/feet\n')
            elif choice == '3':
                print('3 = kilogram/pound\n')
            elif choice == '4':
                print('4 = liters/us gallons\n')
        else:
            welcome()
        return True
        

        



def validate(values):
    """
    Inside try, raise error, if input not equal to,
    1,2,3,4.
    """
    try:
        int(values)
        if values not in ('1', '2', '3', '4'):
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

