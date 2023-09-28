def str_integers(st):
    numbers = []

    splitStr = st.split(',')

    for token in splitStr:
        try:
            num = int(token)
            if num > 0:
                numbers.append(num)
        except ValueError:
            pass

    return numbers

st = input()
numbers = str_integers(st)
print(numbers)