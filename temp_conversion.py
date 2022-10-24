
from lib2to3.pytree import convert
from Classes import Con
from Classes import Con2

def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
    Far = Con(100)
convert_100_to_celsius()
def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
    Far2 = Con(0)
convert_0_to_celsius()
def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    Far3 = Con(34.2)
convert_34_2_to_celsius()

'''
Now, can you convert back?
'''

def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    Cels1=Con2(5)
convert_5_to_fahrenheit()


def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Printout the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively 
    num1= [85.1,Con2(30.2)]
    if max(num1) == 85.1:
        print('85.1 degrees fahrenheit')
    else:
        print('30.2 degrees celsius')
hotter_temp()