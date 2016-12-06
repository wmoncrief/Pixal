from PIL import Image, ImageDraw
from analyzer import get_mode_colors

def generate_image(vid_path,im_path):
    height = 40
    width = 420
    im = Image.new('RGB', (width, height))

    color_list = get_mode_colors(vid_path)

    colors = []
    for i in range(0,len(color_list),3):
        colors.append((color_list[i],color_list[i+1],color_list[i+2]))

    draw = ImageDraw.Draw(im)

    i = 10
    width = 10 + i * 5
    new_coord = [0,0,width,height]
    for color in colors:
        print new_coord
        print width
        width = 10 + i * 5
        draw.rectangle(new_coord,color)
        prev_coord = new_coord
        new_coord = [prev_coord[2],0,prev_coord[2]+width,height]
        i -= 1
    # im.show()
    im.save(im_path)


