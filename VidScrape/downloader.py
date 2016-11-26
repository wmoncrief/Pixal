import pafy
import pandas as pd

def download(url):
	video = pafy.new(url)
	best = video.getbest()
	best.resolution, best.extension
	best.download(quiet=False)

#def load_csv(filepath):
	#df = pd.read_csv(filepath)
	#print df

fp = 'C:\Users\Chris\Desktop\Classes\CSCE489\BigBook\BigBook\VidScrape\country.csv'
df = pd.read_csv(fp)
print df

count = 0 #was looking for the int index but got lazy
for i in df['URL']:
	url = 'https://www.youtube.com' + df['URL'][count] 
	download(url)
	count = count + 1
