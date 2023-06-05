def find_unique_number(list1, list2):
    # Convert the lists to sets
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the difference between the sets
    unique_numbers = set1 - set2
    
    # Return the first unique number found
    if unique_numbers:
        return min(unique_numbers)
    else:
        return None  # No unique number found

