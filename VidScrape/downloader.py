import pafy  # you should run 'pip install youtube-dl' to optimize pafy
import pandas as pd
import os


def download_vid(url,dir):
    try:
        video = pafy.new(url)
        streams = video.streams
        min_res_stream = streams[0]  # we want the lowest resolution video to speed up analysis
        for s in streams:
            if s.resolution < min_res_stream.resolution:
                min_res_stream = s

        print min_res_stream.filename
        min_res_stream.download(quiet=False,filepath=dir + '/' + min_res_stream.filename )  # def load_csv(filepath):
    except BaseException as err:
        print "failed to download a video: " + str(err)



def download_csv(df,dir):
    count = 0  # was looking for the int index but got lazy
    for i in df['URL']:
        url = 'https://www.youtube.com' + df['URL'][count]
        download_vid(url,dir)
        count = count + 1


def download_all():
    genres = ['country', 'edm', 'pop', 'rap', 'rock']
    for genre in genres:
        dir = genre + '_vids'
        if not os.path.exists(dir):
            os.makedirs(dir)

        df = pd.read_csv(genre + '.csv')
        download_csv(df,dir)

download_all()
