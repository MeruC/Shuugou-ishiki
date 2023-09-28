def str_stats(st):
    ucount = 0 
    lcount = 0
    dcount = 0
    wcount = 0

    for char in st:
        if char.isupper():
            ucount += 1
        elif char.islower():
            lcount += 1
        elif char.isdigit():
            dcount += 1
        elif char.isspace():
            wcount += 1

    return ucount, lcount, dcount, wcount

st = input()
ucount, lcount, dcount, wcount = str_stats(st)

print("Uppercase:", ucount)
print("Lowercase:", lcount)
print("Digits:", dcount)
print("Whitespace:", wcount)