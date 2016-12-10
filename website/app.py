# Imports
import os, time, path, pafy, pandas, gen_pic, md_creator, gen_analysis_csv
from PIL import Image, ImageDraw
from analyzer import get_mode_colors
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, send_file
from sklearn.externals import joblib


# create the application
app = Flask(__name__)
app.config.from_object(__name__)

# Return the filename w/ extension
def get_filename_extension(filename):
    index = len(filename) - 1 - filename[::-1].index('.')
    return filename[index:]

# Download the video
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

def gen_classified_string(classified_arr):
    arr = ['Country', 'Edm', 'Pop', 'Rap', 'Rock']
    generated_arr = []
    for x in range(5):
        if classified_arr[x] == 1:
            generated_arr.append(arr[x])
    return ', '.join(generated_arr)
    

# Image gneerated 
@app.route('/image', methods=['GET'])
def image():
    return send_file('dynamic/image.png')

# @app.route('/video', methods=['GET'])
# def image():
    # return send_file('videos/video.png')

@app.route('/', methods=['GET','POST'])
def load_home():
    # If we are receiving a post request
    if request.method == 'POST':
        all_features = ['rating', 'likes', 'dislikes', 'length', 'viewcount', 'colors_1_red', 'colors_1_blue', 'colors_1_green', 'colors_2_red', 'colors_2_blue', 'colors_2_green', 'colors_3_red', 'colors_3_blue', 'colors_3_green', 'colors_4_red', 'colors_4_blue', 'colors_4_green', 'colors_5_red', 'colors_5_blue', 'colors_5_green', 'colors_6_red', 'colors_6_blue', 'colors_6_green', 'colors_7_red', 'colors_7_blue', 'colors_7_green', 'colors_8_red', 'colors_8_blue', 'colors_8_green', 'colors_9_red', 'colors_9_blue', 'colors_9_green', 'colors_10_red', 'colors_10_blue', 'colors_10_green']

        # Get the file and filename
        FILENAME = download_vid(request.form['url'], 'static').encode('ascii')

        # Generate the metadata for the video
        md_creator.get_meta_for_url(request.form['url'])


        # Perform analysis
        video_path = os.path.join('static', FILENAME).encode('ascii')

        # Generate the full data csv
        colors_array = gen_analysis_csv.do_gen(video_path)
        df = pandas.read_csv('metadata/all.csv')
        print df

        # Generate the pixel picture
        gen_pic.generate_image(map(int,colors_array), 'dynamic/image.png')

        # Read in the classifiers
        clf_dir = 'classifiers'
        country_clf = joblib.load(os.path.join(clf_dir, 'country_class.pkl'))
        edm_clf = joblib.load(os.path.join(clf_dir, 'edm_class.pkl'))
        pop_clf = joblib.load(os.path.join(clf_dir, 'pop_class.pkl'))
        rap_clf = joblib.load(os.path.join(clf_dir, 'rap_class.pkl'))
        rock_clf = joblib.load(os.path.join(clf_dir, 'rock_class.pkl'))


        # Perform predictions
        country =  country_clf.predict(df[all_features])[0]
        edm =  edm_clf.predict(df[all_features])[0]
        pop =  pop_clf.predict(df[all_features])[0]
        rap = rap_clf.predict(df[all_features])[0]
        rock = rock_clf.predict(df[all_features])[0]

        # Print the output to console
        print "Output:", country, edm, pop, rap, rock
        genre = gen_classified_string([country, edm, pop, rap, rock])


        print 'FILENAME:', df['filename'][0]
        return render_template('index.html', is_post=True, genre=genre, image_name='image.png', video_name=FILENAME, title=df['filename'])
    else:

        # Other wise we are not 
        return render_template('index.html', is_post=False)

if __name__ == "__main__":
    app.run()
