#Task1
def update_dictionary(dct, key, value):
    # This is to check if the key already exists in the dictionary or to add or update
    if key in dct:
        # Print the original value before updating the dictionary
        print(f"Original value for '{key}': {dct[key]}") # printing original value of the key
    # Update the dictionary with the new key-value pair given
    dct[key] = value
    # Return the updated dictionary
    return dct

#Task2(Scenario1) 
def update_dictionary(dct, key, value):
    # Add or update the key in the dictionary with the given value
    dct[key] = value 
    return dct  # Return the updated dictionary
dct1 = {}  # Given Empty Dictionary
updated_dct1 = update_dictionary(dct1, "name", "Alice") # given command to update the dictionary by adding key "name" with the value "Alice"
print(f"Updated dictionary 1: {updated_dct1}") # print the updated dictionary 

#Task2(Scenario2) 
def update_dictionary(dct, key, value): # Add or update the key in the dictionary with the given value
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    dct[key] = value
    return dct # Return the updated dictionary
# Given values
dct2 = {"age": 25} # Initialize the dictionary
updated_dct2 = update_dictionary(dct2, "age", 26) # Update the age
print(f"Updated dictionary 2: {updated_dct2}")  # Output: Updated dictionary 2: {'age': 26} 
