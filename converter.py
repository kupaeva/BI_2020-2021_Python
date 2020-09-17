import sys
units_dict = ['C', 'F', 'Ra', 'K']

#convert any units to celsia
def to_celsia(units_from, value):
    if units_from == 'F':
        celsia_value = (value - 32) / 1.8
    elif units_from == 'K':
        celsia_value = (value - 273.15)
    elif units_from == 'Ra':
        celsia_value = (value - 491.67) * 5 / 9
    return celsia_value

#convert celsia to any units
def from_celsia(units_to, celsia_value):
    if units_to == 'F':
        units_value = (celsia_value * 1.8) + 32
    elif units_to == 'K':
        units_value = (celsia_value + 273.15)
    elif units_to == 'Ra':
        units_value = (celsia_value + 273.15) * 9 / 5
    return units_value

#input data
print("Hello! I am temperature unit converter. I know next scales: Celsius (C), Fahrenheit (F), Rankine (Ra) and absolute Kelvin temperature (K).")
units_from = input('Please, input original units (C, F, Ra or K)\n').title()
units_to = input('Please, input output units (C, F, Ra or K)\n').title()
value = input('Please, input value\n')

#check input to compliance with acceptable
if units_from not in units_dict or units_to not in units_dict:
    print('Sorry, I do not know your units.')
elif value.isdigit() is not True:
    print('Sorry, I can not understand your value.')
elif units_from == units_to:
    print(value, units_from, 'is', value, units_to)
    sys.exit()

#convert any units to celsia and celsia to any units, print output
else:
    value = float(value)
    if units_from == 'C':
        celsia_value = value
    elif units_from != 'C':
        celsia_value = to_celsia(units_from, value)

    if units_to == 'C':
        print(value, units_from, 'is', celsia_value, units_to)
    elif units_to != 'C':
        celsia_value = from_celsia(units_to, celsia_value)
        print(value, units_from, 'is', celsia_value, units_to)
        