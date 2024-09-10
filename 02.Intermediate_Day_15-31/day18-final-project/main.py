import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('img.jpg', 10)

def getting_color(color):
    color_list = []
    for color_from_list in color:
        r = color_from_list.rgb.r
        g = color_from_list.rgb.g
        b = color_from_list.rgb.b
        color_list.append((r, g, b))
    return color_list

a = getting_color(colors)
print(a)


# for color in colors:
#     # print(i.rgb.r)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     print(r, g, b)

