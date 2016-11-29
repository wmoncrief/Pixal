from analyzer import get_avg_colors
import pandas as pd
from os import listdir

video_dirs = ['country_vids','edm_vids','pop_vids','rap_vids','rock_vids']

for vid_dir in video_dirs:
    directory = '../VidScrape/' + vid_dir
    vid_files = listdir(directory)
    avg_colors = []
    x = 0
    for vid in vid_files:
        if (x > 1):
            break
        color = get_avg_colors(directory + '/' + vid)
        print color
        avg_colors.extend(color)
        x += 1



    headers = ['colors' + str(x+1) for x in range(10)]
    h = []
    for x in headers:
        h.append(x + 'red')
        h.append(x + 'blue')
        h.append(x + 'green')
    cols = ['name'] + h
    df = pd.DataFrame(data=avg_colors,columns=cols)
    df.to_csv(path=vid_dir)
