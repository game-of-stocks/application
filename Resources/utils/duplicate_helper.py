#function to check for duplicates 
def duplicate_counter(array_to_check):
    # Create an empty dictionary to store the count of each element
    all_count = {}
    duplicate_stocks_choosen = []

    # Iterate through the list and count the occurrences of each element
    for element in array_to_check:
        all_count[element] = all_count.get(element, 0) + 1

    # Check if there are any elements with a count greater than 1
    has_duplicates = any(count > 1 for count in all_count.values())
    
    # if there is a duplicate. Output the stocks that are duplicates 
    if has_duplicates == True:
        for key, value in all_count.items():
            if value > 1:
                duplicate_stocks_choosen.append(key)
#         print(f"key: {key}, value: {value}")
        # Join all duplicate stocks choosen into 1 string 
        duplicate_stocks_choosen_string = ', '.join(duplicate_stocks_choosen)
        print(f"You have selected these duplicate stocks {duplicate_stocks_choosen_string} and only one will be included in portfolio")
    else:
        print(f"You have selected the following stocks")
    
    

    

