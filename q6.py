def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    return
i = 0
    # Loop continuously while the index is within the valid bounds of the list
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1  # Increment to check the next item and prevent an infinite loop
        
    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
