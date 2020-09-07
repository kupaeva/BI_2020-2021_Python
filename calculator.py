operator_list = ['+', '-', '/', '//', '*', '**']
n1 = input()
operation = str(input())
n2 = input()
if n1.isdigit() is True and n2.isdigit() is True:
    if operation == "+":
        print(int(n1) + int(n2))
    elif operation == "-":
        print(int(n1) - int(n2))
    elif operation == "*":
        print(int(n1) * int(n2))
    elif operation == "/":
        print(int(n1) / int(n2))
    elif operation == "//":
        print(int(n1) // int(n2))
    elif operation == "**":
        print(int(n1) ** int(n2))
    elif operation not in operator_list:
        print("I don't know this command")
else:
    print('I can not understand your input.')

