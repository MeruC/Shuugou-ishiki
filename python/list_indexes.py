def list_indexes(values, target):
    indexes = []
    index = 0
    for value in values:
        if value == target:
            indexes.append(index)
        index += 1
    return indexes

def list_positives():
    numbers = []
    while True:
        num = int(input("Enter a positive number: "))
        if num > 0:
            numbers.append(num)
        elif num == 0:
             break
    return numbers

values = list_positives()

print(values)

indexes = list_indexes(values, int(input("Enter the target number: "))) 

print(indexes)