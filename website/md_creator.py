import pafy
import pandas as pd
import os


def pull_md(url):  # pull all metadata for each url
    try:
        row = []
        video = pafy.new(url)
        streams = video.streams
        min_res_stream = streams[0]  # this is kept to find correct filename
        for s in streams:
            if s.resolution < min_res_stream.resolution:
                min_res_stream = s
        row.append(min_res_stream.filename)
        if video.author:
            row.append(video.author)
        else:
            row.append(" ")
        try:
            row.append(video.description)
        except BaseException as err:
            row.append(" ")
            print "failed to retrieve description " + str(err)
        if video.viewcount:  # probably a nicer way to do this, but its like 3am
            row.append(video.viewcount)
        else:
            row.append(" ")
        if video.rating:
            row.append(video.rating)
        else:
            row.append(" ")
        if video.likes:
            row.append(video.likes)
        else:
            row.append(" ")
        if video.dislikes:
            row.append(video.dislikes)
        else:
            row.append(" ")
        if video.duration:
            row.append(video.duration)
        else:
            row.append(" ")
        if video.length:
            row.append(video.length)
        else:
            row.append(" ")
        if video.keywords:
            row.append(video.keywords)
        else:
            row.append(" ")
        if video.published:
            row.append(video.published)
        else:
            row.append(" ")

        return row
    except BaseException as err:
        print "failed to load video " + str(err)


def get_meta_for_url(url):
    data = []
    new_row = pull_md(url)
    if new_row:
        data.append(new_row)

    df_md = pd.DataFrame(data)
    df_md.columns = ['filename', 'author', 'description', 'viewcount', 'rating', 'likes', 'dislikes', 'duration',
                     'length', 'keywords', 'published']
    dir = 'metadata'
    if not os.path.exists(dir):
        os.makedirs(dir)
    file_name = os.path.join('metadata', 'md.csv')
    df_md.to_csv(file_name, encoding='utf-8')


'''def create_csv(genre):
    df = pd.read_csv(genre + '.csv')
    data = []
    for row in df['URL']:
        url = 'https://www.youtube.com' + row
        new_row = pull_md(url)
        if new_row:
            data.append(new_row)

    df_md = pd.DataFrame(data)
    df_md.columns = ['filename', 'author', 'description', 'viewcount', 'rating', 'likes', 'dislikes', 'duration',
                     'length', 'keywords', 'published']
    dir = 'metadata'
    if not os.path.exists(dir):
        os.makedirs(dir)
    file_name = 'metadata/' + genre + '_md.csv'
    df_md.to_csv(file_name, encoding='utf-8')


def create_all():
    genres = ['country', 'edm', 'pop', 'rap', 'rock']
    for genre in genres:
        create_csv(genre)


c'''
