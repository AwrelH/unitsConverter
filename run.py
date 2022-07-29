# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def degrees():
    """
    Function to convert celcius to fahrenheit and vice versa.
    """
    print('You have choosen the degrees option')
    print('What do you wish to convert? 1.Fahrenheit or 2.Celcius?')
    input('enter you option(1 or 2): ')
    


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

        


welcome()

