import csv
import pandas as pd
import glob
import os
# Specify the folder path
folder_path = '/Users/jacobhopkins/MT 2024 Leg Expenditures/'

csv_files = glob.glob('/Users/jacobhopkins/MT 2024 Leg Expenditures/*.csv')





# Get a list of all CSV files in the folder

# Create an empty dataframe to store the combined data
big_csv = ""
rejects = []

# Loop through each CSV file and append its contents to the combined dataframe
for file in csv_files:
    with open(file,"r") as csvfile:
        csvreader = csv.reader(csvfile)
        try:
            for row in csvreader:
                for element in row:
                    big_csv += element
                big_csv += "\n"
        except:
            pass


outfile_temp = open("AllExpenditures.csv", 'w')
outfile_temp.write(big_csv)
test = pd.read_csv(big_csv, encoding='latin1', sep='|')

