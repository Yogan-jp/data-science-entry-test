#Task1
def check_divisibility(num, divisor):
    # Below code is to Check if both num and divisor are numeric
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)): # using float incase the number is in decimal
        return "Error: Both num and divisor must be numeric."  
    # Check if divisor is 0 to avoid division by zero
    if divisor == 0:
        return "Error: Divisor cannot be zero." 
    # Return True if num is divisible by divisor, else False
    return num % divisor == 0
  
  # Scenario 1: 10, 2
result1 = check_divisibility(10, 2)
print(f"Is 10 divisible by 2? {result1}") # Expected: True

# Scenario 2: 7, 3
result2 = check_divisibility(7, 3)
print(f"Is 7 divisible by 3? {result2}") # Expected output: False
