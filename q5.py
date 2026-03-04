def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return
# Validate that both inputs are numeric (and not booleans)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))) or isinstance(num, bool) or isinstance(divisor, bool):
        return False
        
    # Handle division by zero to prevent crashes
    if divisor == 0:
        return False
        
    # Modulo operator (%) returns 0 if there is no remainder
    return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
