def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return
# Verify both inputs are numeric types (int or float) and exclude booleans
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))) or isinstance(x, bool) or isinstance(y, bool):
        return -1
    
    # Swap without a third temporary variable using mathematical operations
    x = x + y
    y = x - y
    x = x - y
    
    print(f"Swapped values: x = {x}, y = {y}")

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
