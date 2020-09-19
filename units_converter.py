#test
import sys
units_dict = ['C', 'F', 'Ra', 'K']


# convert any units to Celsius
def to_celsius():
    if units_from == 'F':
        celsius_value_local = (value - 32) / 1.8
    elif units_from == 'K':
        celsius_value_local = (value - 273.15)
    elif units_from == 'Ra':
        celsius_value_local = (value - 491.67) * 5 / 9
    return celsius_value_local


# convert celsius to any units
def from_celsius():
    if units_to == 'F':
        units_value_local = (celsius_value * 1.8) + 32
    elif units_to == 'K':
        units_value_local = (celsius_value + 273.15)
    elif units_to == 'Ra':
        units_value_local = (celsius_value + 273.15) * 9 / 5
    return units_value_local


# input data
print("Hello! I am temperature unit converter. "
      "I know next scales: Celsius (C), Fahrenheit (F), Rankine (Ra) "
      "and absolute Kelvin temperature (K).")
units_from = input('Please, input original units (C, F, Ra or K)\n').title()
units_to = input('Please, input output units (C, F, Ra or K)\n').title()
value = input('Please, input value\n')


# check input to compliance with acceptable
if units_from not in units_dict or units_to not in units_dict:
    print('Sorry, I do not know your units.')
elif value.isdigit() is not True:
    print('Sorry, I can not understand your value.')
elif units_from == units_to:
    print(value, units_from, 'is', value, units_to)
    sys.exit()


# convert any units to celsius and celsius to any units, print output
else:
    value = float(value)
    if units_from == 'C':
        celsius_value = value
    elif units_from != 'C':
        celsius_value = to_celsius()

    if units_to == 'C':
        print(value, units_from, 'is', celsius_value, units_to)
    elif units_to != 'C':
        celsius_value = from_celsius()
        print(value, units_from, 'is', celsius_value, units_to)
