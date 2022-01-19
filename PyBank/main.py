import os
import numpy as np
import csv



budget_csv = os.path.join("resources","budget_data.csv")
total_budget = 0
record_count = 0
budget_changes = [] 
date_changes = []
first_time = True
old_budget = 0
budget_diff = 0



with open(budget_csv,newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)  # skip the headers
   
    
    for row in csvreader:
        if first_time: 
            old_budget = int(row[1]) 
            first_time = False
            
        else: 
            budget_diff = int(row[1]) - old_budget
            budget_changes.append(budget_diff)
            date_changes.append(row[0])
            old_budget = int(row[1])


        total_budget = total_budget + int(row[1])
        #print(row[0])
        record_count = record_count + 1

min_budget = min(budget_changes)
max_budget = max(budget_changes)
ave_budget = sum(budget_changes) / len(budget_changes)


max_month = budget_changes.index(max_budget) 
min_month = budget_changes.index(min_budget)

f = open("budget_analysis.txt","w") 

f.write("Financial Analysis")
f.write('\n')
f.write("----------------------------")
f.write('\n')
f.write(f"Total Months: {record_count}")
f.write('\n')
f.write(f"Total: ${total_budget}")
f.write('\n')
f.write(f"Average Change: ${round(ave_budget, 2)}")
f.write('\n')
f.write(f"Greatest Increase in Profits: {date_changes[max_month]} (${max_budget})")
f.write('\n')
f.write(f"Greatest Decrease in Profits: {date_changes[min_month]} (${min_budget}")
f.close()




print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {record_count}")
print(f"Total: ${total_budget}")
print(f"Average Change: ${round(ave_budget, 2)}")
print(f"Greatest Increase in Profits: {date_changes[max_month]} (${max_budget})")
print(f"Greatest Decrease in Profits: {date_changes[min_month]} (${min_budget}")




