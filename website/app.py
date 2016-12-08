# Imports
import os, time, path, pafy, pandas, gen_pic, md_creator
from PIL import Image, ImageDraw
from analyzer import get_mode_colors
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from sklearn.externals import joblib
import gen_analysis_csv


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

# app.config.from_envvar('FLASK_SETTINGS', silent=True)
def get_filename_extension(filename):
    index = len(filename) - 1 - filename[::-1].index('.')
    return filename[index:]

def do_stuff():
    return "yo"

def download_vid(url,dir):
    try:
        video = pafy.new(url)
        streams = video.streams
        min_res_stream = streams[0]  # we want the lowest resolution video to speed up analysis
        for s in streams:
            if s.resolution < min_res_stream.resolution:
                min_res_stream = s

        print min_res_stream.filename
        FILENAME = 'video' + get_filename_extension(min_res_stream.filename)
        min_res_stream.download(quiet=False,filepath=dir + '/' + FILENAME)  # def load_csv(filepath):
        return FILENAME
        # FILENAME = min_res_stream.filename

    except BaseException as err:
        print "failed to download a video: " + str(err)


def gen_full_csv():
    pass

@app.route('/', methods=['GET','POST'])
def load_home():
    # gen_pic.generate_image('videos/video.3gp', 'static/image.png')
    # return render_template('show_entries.html', entries=entries)
    all_features = ['rating', 'likes', 'dislikes', 'length', 'viewcount', 'colors_1_red', 'colors_1_blue', 'colors_1_green', 'colors_2_red', 'colors_2_blue', 'colors_2_green', 'colors_3_red', 'colors_3_blue', 'colors_3_green', 'colors_4_red', 'colors_4_blue', 'colors_4_green', 'colors_5_red', 'colors_5_blue', 'colors_5_green', 'colors_6_red', 'colors_6_blue', 'colors_6_green', 'colors_7_red', 'colors_7_blue', 'colors_7_green', 'colors_8_red', 'colors_8_blue', 'colors_8_green', 'colors_9_red', 'colors_9_blue', 'colors_9_green', 'colors_10_red', 'colors_10_blue', 'colors_10_green']
    if request.method == 'POST':
        genre = 'Determined Genre'
        print 'Started Download!'
        FILENAME = download_vid(request.form['url'], 'videos').encode('ascii')
        print 'Ended Download!'
        print '****GENERATING IMAGE'
        print '****GENERATING IMAGE'
        print '****GENERATING IMAGE'
        print '****GENERATING IMAGE'
        md_creator.get_meta_for_url(request.form['url'])
        video_path = os.path.join('videos', FILENAME).encode('ascii')
        gen_pic.generate_image(video_path, 'static/image.png')

        print '*****************Generating Full CSV'
        print '*****************Generating Full CSV'
        print '*****************Generating Full CSV'
        print '*****************Generating Full CSV'
        print '*****************Generating Full CSV'
        gen_analysis_csv.do_gen(video_path)
        df = pandas.read_csv('metadata/all.csv')
    
        clf_dir = 'classifiers'
        country_clf = joblib.load(os.path.join(clf_dir, 'country_class.pkl'))
        edm_clf = joblib.load(os.path.join(clf_dir, 'edm_class.pkl'))
        pop_clf = joblib.load(os.path.join(clf_dir, 'pop_class.pkl'))
        rap_clf = joblib.load(os.path.join(clf_dir, 'rap_class.pkl'))
        rock_clf = joblib.load(os.path.join(clf_dir, 'rock_class.pkl'))


        print '***************HERERERERERERERE'
        country =  country_clf.predict(df[all_features])[0]
        edm =  edm_clf.predict(df[all_features])[0]
        pop =  pop_clf.predict(df[all_features])[0]
        rap = rap_clf.predict(df[all_features])[0]
        rock = rock_clf.predict(df[all_features])[0]

        # gen_pic.generate_image('videos/video.3gp', 'static/image.png')
        return render_template('index.html', is_post=True, genre=genre, show_pic=True, rock=rock, edm=edm, pop=pop, rap=rap, country=country)
    else:
        return render_template('index.html', is_post=False)

    # if not session.get('logged_in'):
        # abort(401)
    # db = get_db()
    # db.execute('insert into entries (title, text) values (?, ?)',
    #              [request.form['title'], request.form['text']])

if __name__ == "__main__":
    app.run()
