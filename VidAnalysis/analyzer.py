import skvideo.io
import skvideo.datasets
from os import path
import numpy as np

# you need to install ffmpeg to run this on mac.
# i used 'brew install ffmpeg' to install.

test_vid = path.abspath('videoplayback.3gp')
videogen = skvideo.io.vreader(test_vid)
i = 0
for frame in videogen:
    print i
    i += 1
    if frame is not None:
        avg_row_color = np.mean(frame,axis=1)
        avg_column_color = np.mean(avg_row_color,axis=0)
        print avg_column_color