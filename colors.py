import random

# colors
white = (255, 255, 255)
cream = (255, 251, 222)
black = (0, 0, 0)
grey = (99, 96, 96)
really_red = (255, 0, 0)
shady_red = (207, 94, 74)
earth_green = (0, 255, 0)
deep_green = (80, 120, 76)
really_blue = (0, 0, 255)
deep_blue = (44, 46, 163)
bright_yellow = (251, 255, 15)
shady_yellow = (197, 199, 87)
bright_pink = (255, 0, 255)
shady_pink = (163, 59, 163)
purple = (165, 2, 250)
deep_purple = (99, 36, 133)
toothpaste = (0, 255, 255)
ice = (185, 232, 234)

# dictionary for generating a random color
col = {1: white, 2: cream, 3: black, 4: grey, 5: really_red, 6: shady_red, 7: earth_green, 8: deep_green, 9: really_blue, 10: deep_blue, 11: bright_yellow, 12: shady_yellow, 13: bright_pink, 14: shady_pink, 15: purple, 16: deep_purple, 17: toothpaste, 18: ice}


# randomColor function to select a random color
def random_color(dictt=col, excludes={}):
	new_dictt = {no: color for no, color in zip(dictt.keys(), dictt.values()) if color not in excludes}
	color = random.choice(list(new_dictt.values()))
	return color
