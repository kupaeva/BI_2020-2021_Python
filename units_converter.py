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