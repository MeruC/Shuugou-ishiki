def get_address(st):
    try:
        words = st.split()
        
        # Check for the right length
        if len(words) < 6:
            raise ValueError("Input has too few words")
        elif len(words) > 6:
            raise ValueError("Input has too many words")

        name = ' '.join(words[:2])
        street = ' '.join(words[2:4])
        city = ' '.join(words[4:6])
        postal_code = ' '.join(words[-2:])

        return (name, street, city, postal_code)
    
    except ValueError as e:
        return str(e)
    
st = input("Enter the address: ")
address = get_address(st)
print(address)


# David Brown King St Waterloo, ON Q1Q 1Q1

# Duran Duran Rock Ave Kitchener, ON ROK ON3

