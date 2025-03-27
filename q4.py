#Task1
def string_reverse(s): # This is to check if s is a valid string
    if not isinstance(s, str):
        return "Error: Input must be a string." # Return an error message if input is not a string
    # Reverse the string using slicing and return it
    return s[::-1] # It uses slicing [::-1] reverses the string

#Task2
def string_reverse(s): #This is to check if s is a string
    if not isinstance(s, str):
        return "Error: Input must be a string."  # Return an Error message if input is not a string
    # Reverse the string using slicing and return it
    return s[::-1]  # It uses slicing [::-1] reverses the string

# Scenario 1: Reversing "Hello World"
s1 = "Hello World"  # Input string
reversed_s1 = string_reverse(s1)  # Call the function
print(f"Reversed string 1: {reversed_s1}")  # Print the reversed string

# Scenario 2: Reversing "Python"
s2 = "Python"  # Input string
reversed_s2 = string_reverse(s2)  # Call the function
print(f"Reversed string 2: {reversed_s2}")  # Print the reversed string
