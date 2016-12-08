# Imports
import os, time
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import pandas

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


def do_stuff():
    time.sleep(5)
    return "yo"

@app.route('/', methods=['GET','POST'])
def load_home():
    # return render_template('show_entries.html', entries=entries)

    if request.method == 'POST':
        print "if ran"
        print request.form['url']
        print do_stuff()
    return render_template('index.html')

    # if not session.get('logged_in'):
        # abort(401)
    # db = get_db()
    # db.execute('insert into entries (title, text) values (?, ?)',
    #              [request.form['title'], request.form['text']])

if __name__ == "__main__":
    app.run()
