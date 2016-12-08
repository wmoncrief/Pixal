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
    for row in df['URL']:
        url = 'https://www.youtube.com' + row
        download_vid(url,dir)


def download_all():
    genres = ['country', 'edm', 'pop', 'rap', 'rock']
    for genre in genres:
        dir = genre + '_vids'
        if not os.path.exists(dir):
            os.makedirs(dir)

        df = pd.read_csv(genre + '.csv')
        download_csv(df,dir)

def download_all2():
    genres = ['country', 'edm', 'pop', 'rap', 'rock']
    for genre in genres:
        dir = '../Videos2/' + genre + '_vids'
        if not os.path.exists(dir):
            os.makedirs(dir)

        df = pd.read_csv(genre + '2.csv')
        download_csv(df,dir)

download_all2()
