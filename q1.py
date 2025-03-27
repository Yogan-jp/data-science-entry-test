#Task1
def swap_and_print_if_numeric(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)): # To check whether variable is integer and also whether it is decimal number
        # Using Arithmetic swap to check input given is integer or not
        x = x + y  # x now has combine X and Y value together
        y = x - y  # y now has original x
        x = x - y  # x now has original y
        print(f"Swapped values: x = {x}, y = {y}")  # using Printf places output on standard output and swapped values
        return x, y
    else:
        return -1  # output returned -1 if it is non numeric
#Task2
x="Apple"
y=10
def swap_and_print_if_numeric(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)): # To check whether variable is integer and also whether it is decimal number
        # Using Arithmetic swap to check input given is integer or not
        x = x + y  # x now has combine X and Y value together
        y = x - y  # y now has original x
        x = x - y  # x now has original y
        print(f"Swapped values: x = {x}, y = {y}")  # using Printf places output on standard output and swapped values
        return x, y
    else:
        return -1  # output returned -1 if it is non numeric
#Task3
x=9
y=17
def swap_and_print_if_numeric(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)): # To check whether variable is integer and also whether it is decimal number
        # Using Arithmetic swap to check input given is integer or not
        x = x + y  # x now has combine X and Y value together
        y = x - y  # y now has original x
        x = x - y  # x now has original y
        print(f"Swapped values: x = {x}, y = {y}")  # using Printf places output on standard output and swapped values
        return x, y
    else:
        return -1  # output returned -1 if it is non numeric
