import sys
sys.path.append('C:\Users\Chris\Desktop\Classes\CSCE489\BigBook\mps-youtube-pafy-388db45') #fixes a local temp package issue

import pafy
import pandas as pd
import csv

def download(url):
	video = pafy.new(url)
	video.download(quiet=False)

def load_csv(filepath):
	df = pd.read_csv(filepath)
    #unfinished

url = "https://www.youtube.com/watch?v=UtZBA1bVbcs" #single case example
download(url)

#video = pafy.new(url)
#best = video.getbest()
#best.resolution, best.extension
#best.download(quiet=False)