colors = (("green","#008000"),("blue","#0000FF"))
color_dictionary = {}
for key, value in colors:
    color_dictionary.update({f"{key}":f"{value}"})

print(color_dictionary)

# Or:
colors = (("green","#008000"),("blue","#0000FF"))
color_dictionary = dict(colors)
print(color_dictionary)