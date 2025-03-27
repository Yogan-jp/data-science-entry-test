#Task1
def find_first_negative(lst):
    index = 0    # Initialize an index variable to run through the list
    while index < len(lst): # Use a while loop command to run through the list
        if lst[index] < 0: # this is to check condition if the number is less than 0 to find if there is a negative number.
            return lst[index]  # Return call the first negative number found in the list
        index += 1  # this code is to move to the next element in the list     
    return "No negatives" # If no negative number is found, return the message No Negatives

#Task2 
# Scenario 1: [3, 5, -1, 7, -2, 8]
lst1 = [3, 5, -1, 7, -2, 8] # list given numbers 
result1 = find_first_negative(lst1) # to find first negative number in the list 
print(f"First negative number: {result1}")  # Expected result to get -1 in the list and print -1

# Scenario 2: [2, 10, 7, 0]
lst2 = [2, 10, 7, 0] # list Given numbers
result2 = find_first_negative(lst2) # to find first negative number in the list 
print(f"First negative number: {result2}")  # Expected result: No negatives since no negative numbers in the list
