import glob
import os
import numpy as np
import sys

current_dir = "images"
split_pct = 10;
file_train = open("train.txt", "w")  
file_val = open("test.txt", "w")  
counter = 1  
index_test = round(100 / split_pct)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if counter == index_test:
                counter = 1
                file_val.write("dataset" + "/" + current_dir + "/" + title + '.jpg' + "\n")
        else:
                file_train.write("dataset" + "/" + current_dir + "/" + title + '.jpg' + "\n")
                counter = counter + 1
counter = 1
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.png")):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if counter == index_test:
                counter = 1
                file_val.write("dataset" + "/" + current_dir + "/" + title + '.png' + "\n")
        else:
                file_train.write("dataset" + "/" + current_dir + "/" + title + '.png' + "\n")
                counter = counter + 1
file_train.close()
file_val.close()