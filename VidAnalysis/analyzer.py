import skvideo.io
import skvideo.datasets
from os import path
import numpy as np
from math import ceil


# you need to install ffmpeg to run this on mac.
# i used 'brew install ffmpeg' to install.


# returns a list of the average color in each of ten sections of the video
def get_avg_colors(vid_file_name):
    test_vid = path.abspath(vid_file_name)
    video = skvideo.io.vreader(test_vid)

    frame_colors = []
    i = 0
    for frame in video:
        i += 1
        if frame is not None:
            avg_row_color = np.mean(frame,axis=1)
            avg_column_color = np.mean(avg_row_color,axis=0)
            frame_colors.append(tuple(avg_column_color))

    # now to split the data into 10 groups
    total_frames = float(len(frame_colors))
    split_len = int(ceil(total_frames / 10))

    avg_list = []
    i = 0
    while i < total_frames:
        subsection = frame_colors[i:i+split_len]
        subsection_avg_color = get_avg_color_tuple(subsection)
        avg_list.append(subsection_avg_color)
        i += split_len

    # quick way to get flattened list
    l = []
    for x in avg_list:
        l.extend(list(x))
    return l


def get_avg_color_tuple(colors):
    r = sum(colors[0]) / float(len(colors[0]))
    g = sum(colors[1]) / float(len(colors[1]))
    b = sum(colors[2]) / float(len(colors[2]))
    return r,g,b


# print get_avg_colors('blankSpace.mp4')