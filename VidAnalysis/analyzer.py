import skvideo.io
import skvideo.datasets
from os import path
import numpy as np
from math import ceil
import scipy.stats


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
            avg_row_color = np.mean(frame, axis=1)
            avg_column_color = np.mean(avg_row_color, axis=0)
            frame_colors.append(tuple(avg_column_color))

    # now to split the data into 10 groups
    total_frames = float(len(frame_colors))
    split_len = int(ceil(total_frames / 10))

    avg_list = []
    i = 0
    while i < total_frames:
        subsection = frame_colors[i:i + split_len]
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
    return r, g, b


def is_grey(color_list):
    if max(color_list) - min(color_list) <= 10:
        return True
    return False


def get_nongrey_mode(colors):
    if not colors:
        return None
    mode_str = scipy.stats.mode(colors).mode[0]
    mode = unhash_color_list(mode_str)
    if is_grey(mode):
        return get_nongrey_mode([x for x in colors if x != mode_str])
    else:
        return mode


def gen_b_and_w_modes():
    # this function is for films that are black and white.
    # we have discarded all of their non-color data, so we will use
    # this as an average for them.
    b_and_w = []
    for x in range(30):
        if x % 3 == 0:
            b_and_w.append(8 * x)
        if x % 3 == 1:
            b_and_w.append(8 * (x - 1))
        if x % 3 == 2:
            b_and_w.append(8 * (x - 2))
    return [b_and_w[i:i + 3] for i in range(0, len(b_and_w), 3)]


def get_most_common_modes(frame_modes):
    if not frame_modes:  # shows that it was black and white video
        return gen_b_and_w_modes()

    most_common_modes = []
    hashed_frame_modes = [hash_color_list(x) for x in frame_modes]

    for i in range(10):
        modes = scipy.stats.mode(hashed_frame_modes).mode
        for m in modes:  # could be more than one mode (tied)
            m = m.tolist()
            most_common_modes.append(m)
            for j in range(len(frame_modes)):
                if j < len(hashed_frame_modes) and hashed_frame_modes[j] == m:
                    hashed_frame_modes.pop(j)
    return [unhash_color_list(x) for x in most_common_modes]


# hashes are helpful for taking the mode of RGB values (since scipy mode only works on single element)
def hash_color_list(colors):
    hash = ""
    for col in colors:
        rounded = int(ceil(col / 10.0) * 10)
        hash += str(rounded).zfill(3)
    return hash


def unhash_color_list(color_hash):
    l = []
    for i in range(0, len(color_hash), 3):
        c = color_hash[i:i + 3]
        l.append(int(c))
    return l


FRAME_INTERVAL = 100  # only analyze every nth frame
PIXEL_INTERVAL = 20  # only analyze every nth pixel in each frame


def get_mode_colors(vid_file_name):
    test_vid = path.abspath(vid_file_name)
    video = skvideo.io.vreader(test_vid)

    frame_colors = []
    i = 0
    for frame in video:
        i += 1
        if i % PIXEL_INTERVAL == 0:
            if frame is not None:
                for x in range(0, len(frame) - PIXEL_INTERVAL, PIXEL_INTERVAL):
                    for y in range(0, len(frame[0]) - PIXEL_INTERVAL, PIXEL_INTERVAL):
                        frame_colors.append(hash_color_list(frame[x][y]))

    # get non-grey mode from each frame that we have looked at
    frame_modes = []
    for f_col in frame_colors:
        mode = get_nongrey_mode(f_col)
        if mode is not None:
            frame_modes.append(mode)
    del frame_colors

    most_common_modes = get_most_common_modes(frame_modes)

    # quick way to get flattened list
    l = []
    for i in range(10):
        l.extend(list(most_common_modes[i]))
    return l


x = get_mode_colors('bare.mp4')
print x
