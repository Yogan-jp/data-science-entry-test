#Task1
def replace_all_occurrences(lst, find_val, replace_val):
    # Loop through the list and replace occurrences of find_val with replace_val
    for i in range(len(lst)): # iterate over sequence of numbers
        if lst[i] == find_val: # Find the value
            lst[i] = replace_val # Replace with given value
    return lst
  
  #Task2(Scenario1)
lst1 = [1, 2, 3, 4, 2, 2] # Given list of numbers
find_val1 = 2 # Find value 2 in the list 
replace_val1 = 5 # Replace 2 in the list to value 5
updated_lst1 = replace_all_occurrences(lst1, find_val1, replace_val1) # Replace all occurance and print the updated list
print(f"Updated list 1: {updated_lst1}")

#Task2(Scenario2)
lst2 = ["apple", "banana", "apple"] # Given list of fruits (Strings)
find_val2 = "apple" # Find value apple in the list 
replace_val2 = "orange"  # Replace apple in the list to orange
updated_lst2 = replace_all_occurrences(lst2, find_val2, replace_val2)
print(f"Updated list 2: {updated_lst2}") # Replace all occurance and print the updated list
