#read all CSV files
# import necessary libraries
from sys import displayhook
import pandas as pd
import os
import glob

# Folder Path
path = "your path"

# Change the directory
os.chdir(path)

# use glob to get all the csv files
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))


# loop over the list of csv files
for f in csv_files:

	# read the csv file
	df = pd.read_csv(f)

	# print the location and filename
	print('Location:', f)
	print('File Name:', f.split("\\")[-1])

	# print the content
	print('Content:')
	displayhook(df)
	print()
