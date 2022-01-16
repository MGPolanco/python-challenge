from distutils.command.build_scripts import first_line_re
import os
import csv

election_csv = os.path.join("resources","/Users/mindy/Documents/GitHub/python-challenge/PyPoll/resources/election_data.csv")

total_votes = (0)
first_time = True
old_count = (0)

with open(election_csv,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #sortedlist = sorted(csvreader, key=lambda row: row[1], reverse = True)
    #print(sortedlist)

    for row in csvreader:
        if first_time: 
            old_count = int(row[1])
            first_time = False

        else:  
               
