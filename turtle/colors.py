import colorgram as cg

c_list = []
colors = cg.extract('hirst.jpeg', 20)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    c_list.append(new_color)