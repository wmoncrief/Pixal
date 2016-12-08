from analyzer import get_mode_colors
import pandas as pd
from os import listdir,fsync, path
import csv
import time

def gen_new_headers(old_headers):
    headers = ['colors_' + str(x+1) + '_' for x in range(10)]
    h = []
    for x in headers:
        h.append(x + 'red')
        h.append(x + 'blue')
        h.append(x + 'green')
    return old_headers + h + ['genre']

def do_gen(filename):
    meta_csv_file = open('metadata/md.csv', 'r')
    meta_csv = csv.reader(meta_csv_file)
    new_csv_file = open('metadata/all.csv', 'w')
    new_csv = csv.writer(new_csv_file)
    
    old_headers = meta_csv.next()
    new_headers = gen_new_headers(old_headers)
    
    new_csv.writerow(new_headers)
    
    color = get_mode_colors(path.join('videos', filename))
    # color = [item for sublist in color for item in sublist]
    print color
    color = map(str, map(int, color))
    new_row = meta_csv.next() + color
    print ''
    print new_row
    # write the file as we go to avoid losing data
    new_csv.writerow(new_row)
    new_csv_file.flush()
    fsync(new_csv_file.fileno())
    time.sleep(1)
    new_csv_file.close()
    meta_csv_file.close()
