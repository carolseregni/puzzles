def phone_number(number):
    # Remove Symbols    
    number = number.replace("-","")
    number = number.replace(".","")
    number = number.replace("(","")
    number = number.replace(")","")
    number = number.replace("+1","")
    
    # Remove Spaces and Reformat as Int
    number = number.replace(" ","")
    
    # Remove Country Code
    if len(number) == 10:
        number = number[1:]
    
    # Replace Int
    number = int(number)
    
    # Print Numbers
    return(number)
