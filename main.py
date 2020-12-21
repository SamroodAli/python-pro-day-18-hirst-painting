import colorgram
from collections import namedtuple
colors = colorgram.extract("images/image.jpg", 35)
colors_tuples = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_tuples.append((r, g, b))

