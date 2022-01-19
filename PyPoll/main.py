import os
import csv

election_csv = os.path.join("resources","election_data.csv")

total_votes = 0
candidates_vote = {} #dict to store all candidates votes


with open(election_csv,newline='') as csvfile:

        csvreader = csv.reader(csvfile,delimiter=",")
        next(csvreader)

    
        for row in csvreader:
            #total vote count
            total_votes = total_votes + 1 #increment the count by one
            
            #get candidate votes
            candidate = row[2] #retrieve candidate name from column index 02

            #if candidate is in dict, then increment candidate vote by one..{'Khan': 18} 
            #...else add new key of candidate to dict {'Khan': 1}
            if candidate in candidates_vote:
                candidates_vote[candidate]= candidates_vote[candidate] + 1
            else:
                candidates_vote[candidate] = 1 


# get all the candidate names from dict
candidate_names = candidates_vote.keys() #["Khan", "Correy", "Li", "Tooley"]
candidates_percent = {}
winner = None
winner_votes = 0

for name in candidate_names: #start looping through all the names in the list
    vote = candidates_vote[name] #use the name to get candidate vote from "candidates_vote" dict
    percent = (vote/total_votes)*100
    
    #store the percentage into the "candidates_percent" dict 
    candidates_percent[name] = round(percent, 4)
        
    #keep testing for the highest vote, and store the winner info into the winner variables
    if vote > winner_votes:
        winner = name
        winner_votes = vote

Khan = candidates_percent['Khan'], candidates_vote['Khan']
Correy = candidates_percent['Correy'], candidates_vote['Correy']
Li = candidates_percent['Li'],candidates_vote['Li']
Tooley = candidates_percent["O'Tooley"], candidates_vote["O'Tooley"]



print('Election Results\n----------------------------')
print(f'Total votes: {total_votes}\n----------------------------')
print(f"Khan", candidates_percent['Khan'], candidates_vote['Khan'])
print(f"Correy", candidates_percent['Correy'], candidates_vote['Correy'])
print(f"Li", candidates_percent['Li'], candidates_vote['Li'])
print(f"O'Tooley", candidates_percent["O'Tooley"], candidates_vote["O'Tooley"])
print('----------------------------')
print(f"Winner:", winner)

f = open("election_data_1.text", "w")

print('Election Results\n----------------------------',file=f)
print(f'Total votes: {total_votes}\n----------------------------',file=f)
print(f"Khan", candidates_percent['Khan'], candidates_vote['Khan'],file=f)
print(f"Correy", candidates_percent['Correy'], candidates_vote['Correy'],file=f)
print(f"Li", candidates_percent['Li'], candidates_vote['Li'],file=f)
print(f"O'Tooley", candidates_percent["O'Tooley"], candidates_vote["O'Tooley"],file=f)
print('----------------------------',file=f)
print(f"Winner:", winner,file=f)
f.close()


