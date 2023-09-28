def color_frequencies(*colors):
    frequencies = {}
    for color in colors:
        if color in frequencies:
            frequencies[color] += 1
        else:
            frequencies[color] = 1
    return frequencies

#INPUT VERSION
colors = []
while True:
    try:
        color = input("Enter a color (or 'stop' to finish): ").strip().lower()
        if color == "stop":
            break
        elif color.isalpha():
            colors.append(color)
        else:
            raise ValueError("Invalid input. Please enter a valid color name.")
    except ValueError as e:
        print(e)

#PRE DEFINED VERSION
#colors = ("red", "green", "blue", "red", "blue")

result = color_frequencies(*colors)
print(result)
