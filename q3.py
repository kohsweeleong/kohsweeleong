def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return
# Check if the key is already present in the dictionary
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
        
    # Set the new value (creates the key if it didn't exist, updates if it did)
    dct[key] = value
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
