operator_list = ['+', '-', '/', '//', '*', '**']
n1 = input('First number: ')
operation = input('Operator: ')
n2 = input('Second number: ')
if n1.isdigit() is True and n2.isdigit() is True:
    n1 = float(n1)
    n2 = float(n2)
    if operation == "+":
        print(n1 + n2)
    elif operation == "-":
        print(n1 - n2)
    elif operation == "*":
        print(n1 * n2)
    elif operation == "/":
        print(n1 / n2)
    elif operation == "//":
        print(n1 // n2)
    elif operation == "**":
        print(n1 ** n2)
    elif operation not in operator_list:
        print("I don't know this command. ")
else:
    print('I can not understand your input.')
