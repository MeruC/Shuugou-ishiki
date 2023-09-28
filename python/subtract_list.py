def subtract_lists(minuend, subtrahend):
    for value in subtrahend:
        if value in minuend:
            minuend.remove(value)

def list_positives():
    numbers = []
    while True:
        num = int(input("Enter a positive number: "))
        if num > 0:
            numbers.append(num)
        elif num == 0:
             break
    return numbers

print("Values for Minuend")
minuend = list_positives()
print("Values for Subtrahend")
subtrahend = list_positives()

subtract_lists(minuend, subtrahend)

print(minuend)