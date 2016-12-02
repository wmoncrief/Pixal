import os
from subprocess import call
import time


genres = ['country', 'edm', 'pop', 'rap', 'rock']

#  run this in the same directory that holds all your video directories, so it should be
#  a sibling of country_vids, edm_vids, etc.

for genre in genres:
    full_vids = os.listdir(genre + '_vids')
    if not os.path.exists('compressed_' + genre):
        os.makedirs('compressed_' + genre)
    for old_vid in full_vids:
        old_vid_path = genre + '_vids/' + old_vid
        new_vid_path = 'compressed_' + genre + '/' + old_vid
        print ' '.join(
            ["ffmpeg", "-i", old_vid_path, "-s", "250x250", "-b:a", "200k", "-vcodec", "mpeg4", "-acodec", "copy",
             new_vid_path])

        call(["ffmpeg", "-i", old_vid_path, "-s", "250x250", "-b:a", "200k", "-vcodec", "mpeg4", "-acodec", "copy",
              new_vid_path])

        time.sleep(7)  # to prevent my computer from blowing up
print 'hi'
