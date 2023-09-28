def color_frequencies(*colors):
    frequencies = {}
    for color in colors:
        if color in frequencies:
            frequencies[color] += 1
        else:
            frequencies[color] = 1
    return frequencies

colors = ("red", "green", "blue", "red", "blue")
result = color_frequencies(*colors)
print(result)