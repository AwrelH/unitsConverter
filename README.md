# Units Converter

The units converter is a python terminal program that takes values from the user and converts it to other units.

[The live site is found here](https://units-converter-awrel.herokuapp.com/)

![the terminal](assets/forReadme/readmeIntro.PNG)

# How to use

The program is very straightforward. You will as a user be presented with 5 options. Four of them equals conversion choices. 
- Celsius / Fahrenheit
- Meters / feet
- Kilos / pounds
- Liters / gallons

# walkthrough of the program

# Testing
I have tested the program for each of the steps and tried to commit as often as I could. This has helped to avoid bugs. 

## Bugs
Some of the bugs that I have come across wasn't too hard to handle. Foremost it was string input that couldn't be handled since they weren't integers or floats. That was easily handled by using the int() or float()-function in the equations.

one of the last bugs that I found was that after I ran a program e.g degrees(), and came back to main-menu and choose the exit-option was that I didn't exit the program. Instead, I was stuck in a loop, with the menu. I then tried to do a separate function just to exit while not being in the while-loop of the choices. Didn't really help, removed some while-loop, but still the same result. After a while I went for the built-in function exit() that did the trick. I would count this as a bug that was not solved.  




## Validation
I validated my code via the pep8 online check, (http://pep8online.com/) without any error messages. This was possible by continuously reading the 'problems' message that was presented in the Gitpod IDE. 

# Deployment


# Credit


