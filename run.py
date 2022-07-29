import colorama
from colorama import Fore
colorama.init(autoreset=True)


def retry_message():
    """
    Prints a retry message.
    """
    print("\nWish to test out some other values?")
    print("y/n?")


def answers(answer):  # output answer to calculations
    print('###############################################')
    print(f"{Fore.YELLOW} {answer}")
    print('###############################################')


def error_message():
    print(f'{Fore.RED}invalid input, try again')


def degrees():
    """
    Function to convert celcius to fahrenheit and vice versa.
    """
    print("You have choosen the degrees option")
    print("What do you wish to convert? 1.Fahrenheit or 2.Celcius?")
    option = input("enter you option(1 or 2): ")
    if option == "1":
        print("\nFahrenheit it is...")
        option_value = input("Write down a temperature: ")
        if not option_value.isdigit():
            error_message()
            degrees()
        else:
            cel_value = round((int(option_value) - 32) * 5 / 9, 2)
            answer = f"\t{option_value} F equals {cel_value} deg. Celcius"
            answers(answer)
            retry_message()
            retry_answer = input()
            if retry_answer == "y":
                degrees()
            else:
                welcome()
    elif option == "2":
        print("\nCelcius it is...")
        option_value = input("Write down a temperature: ")
        if not option_value.isdigit():
            error_message()
            degrees()
        else:
            fahr_value = round((int(option_value) * 1.8) + 32, 2)
            answer = f"\t{option_value} C equals {fahr_value} deg. Fahrenheit"
            answers(answer)
            retry_message()
            retry_answer = input()
            if retry_answer == "y":
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
    print("You have choosen the meters option")
    print("What do you wish to convert? 1.Feet or 2.Meters?")
    option = input("enter you option(1 or 2): ")
    if option == "1":
        print("\nFeet it is...")
        option_value = input("How many feet: ")
        if not option_value.isdigit():
            error_message()
            meters()
        else:
            meter_value = round(float(option_value) / 3.2808399, 2)
            answer = f"\t{option_value} feet equals {meter_value} meters"
            answers(answer)
            retry_message()
            retry_answer = input()
            if retry_answer == "y":
                meters()
            else:
                welcome()
    elif option == "2":
        print("\nmeters it is...")
        option_value = input("How many meters: ")
        if not option_value.isdigit():
            error_message()
            meters()
        else:
            feet_value = round(float(option_value) * 3.2808399, 2)
            answer = f"\t{option_value} meter(s) equals {feet_value} feet"
            answers(answer)
            retry_message()
            retry_answer = input()
            if retry_answer == "y":
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
    print("You have choosen the kilos option")
    print("What do you wish to convert? 1.Kilos or 2.Pounds?")
    option = input("enter you option(1 or 2): ")
    if option == "1":
        print("\nKilos it is...")
        option_value = input("How many kilos: ")
        if not option_value.isdigit():
            error_message()
            kilos()
        else:
            pounds_value = round(float(option_value) * 2.20462262, 2)
            answer = f"\t{option_value} kilo(s) equals {pounds_value} pound(s)"
            answers(answer)
            retry_message()
            retry_answer = input()
            if retry_answer == "y":
                kilos()
            else:
                welcome()
    elif option == "2":
        print("\nPounds it is...")
        option_value = input("How many pounds: ")
        if not option_value.isdigit():
            error_message()
            kilos()
        else:
            kilos_value = round(float(option_value) / 2.20462262, 2)
            answer = f"\t{option_value} pound(s) equals {kilos_value} kilo(s)"
            answers(answer)
            retry_message()
            retry_answer = input()
            if retry_answer == "y":
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
    print("You have choosen the liters option")
    print("What do you wish to convert? 1.Liters or 2.Gallons?")
    option = input("enter you option(1 or 2): ")
    if option == "1":
        print("\nLiters it is...")
        option_value = input("How many liters: ")
        if not option_value.isdigit():
            error_message()
            liters()
        else:
            gallons_value = round(int(option_value) / 3.78541178, 2)
            answer = f"\t{option_value} liters equals {gallons_value} gallons"
            answers(answer)
            retry_message()
            retry_answer = input()
            if retry_answer == "y":
                degrees()
            else:
                welcome()
    elif option == "2":
        print("\nGallons it is...")
        option_value = input("How many gallons: ")
        if not option_value.isdigit():
            error_message()
            liters()
        else:
            liters_value = round(int(option_value) * 3.78541178, 2)
            answer = f"\t{option_value} gallons equals {liters_value} liters"
            answers(answer)
            retry_message()
            retry_answer = input()
            if retry_answer == "y":
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
    message = """\n
        welcome to the unit converter!\n
        Units you can convert:\n
        1 = celcius/fahrenheit\n
        2 = meters/feet\n
        3 = kilogram/pound\n
        4 = liters/us gallons\n
        5 = exit the program
        make your choice my entering one of the above(1-5) options.
        """
    print(f'{Fore.BLUE} + {message}')
    while True:
        choice = input()
        if validate(choice):
            if choice == "1":
                degrees()
            elif choice == "2":
                meters()
            elif choice == "3":
                kilos()
            elif choice == "4":
                liters()
            elif choice == "5":
                print("Thank you for testing the program!")
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
        if values not in ("1", "2", "3", "4", "5"):
            raise ValueError(f"1,2,3,4,5 are valid values, you typed {values}")
    except ValueError as e:
        print(f'{Fore.RED}Invalid input: {e}, try again.\n')
        return False
    return True


def validate_opt(values):
    """
    Raises an error if values not 1 or 2.
    """
    try:
        if values not in ("1", "2"):
            raise ValueError(f"1,2 are valid values, you typed {values}")
    except ValueError as e:
        print(f"{Fore.RED}Invalid input: {e}, try again.\n")
        return False
    return True


def main():
    """
    main function starts the program
    """
    welcome()


main()
