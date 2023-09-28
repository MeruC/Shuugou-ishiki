def list_positives():
    numbers = []
    while True:
        num = int(input("Enter a positive number: "))
        if num > 0:
            numbers.append(num)
        elif num == 0:
             break
    return numbers

positive_numbers = list_positives()

print(positive_numbers)