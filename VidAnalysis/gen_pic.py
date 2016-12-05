from PIL import Image, ImageDraw
import numpy as np
from analyzer import get_mode_colors

height = 40
im = Image.new('RGB', (400, height))

color_list = [20, 0, 0, 240, 230, 200, 250, 240, 210, 50, 40, 30, 50, 30, 30, 40, 30, 20, 220, 230, 240, 260, 260, 240, 20, 10, 0, 80, 80, 50]
# from barefoot blue jean night
colors = []
for i in range(0,len(color_list),3):
    colors.append((color_list[i],color_list[i+1],color_list[i+2]))

draw = ImageDraw.Draw(im)
i = 10
new_coord = [0,0,40,40]
prev_coord = []
# for color in colors:
width = 10 + i * 2
# draw.rectangle(new_coord,colors[1])
prev_coord = new_coord
new_coord = [0,20,0,height]
print new_coord
draw.rectangle(new_coord,colors[2])
i -= 1
im.show()
