import os
import csv
import collections
from collections import Counter

pypoll_csv = os.path.join("Resources", "election_data.csv")

candidates_dict = {}


with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        candidate=row[2]
        if not candidate in candidates_dict.keys():
            candidates_dict[candidate]=0
        candidates_dict[candidate]+=1
total_votes=0
winner= ""
winner_votes=0
    

for candidate in candidates_dict:
    total_votes+=candidates_dict[candidate]
    if candidates_dict[candidate] > winner_votes:
        winner_votes=candidates_dict[candidate]
        winner=candidate    
        
    
    



output_path = os.path.join("Analysis" ,"voter.txt")
with open(output_path, 'w') as csvfile:
    csvfile.write(f"Election Result\n")
    print(f"Election Result")
    csvfile.write(f"-------------------------------------------------\n")
    print(f"-------------------------------------------------\n")

    csvfile.write(f"Total Votes:  {total_votes}\n")
    print(f"Total Votes:  {total_votes}\n")
    csvfile.write(f"-------------------------------------------------\n")
    print(f"-------------------------------------------------\n")
    for candidate in candidates_dict:
        csvfile.write(f"{candidate}: {round(candidates_dict[candidate]/total_votes,5)*100}% ({candidates_dict[candidate]})\n")
        print(f"{candidate}: {round(candidates_dict[candidate]/total_votes,5)*100}% ({candidates_dict[candidate]})\n")
    csvfile.write(f"-------------------------------------------------\n")
    print(f"-------------------------------------------------\n")
    csvfile.write(f"Winner:  {winner}\n")
    print(f"Winner:  {winner}\n")
    csvfile.write(f"-------------------------------------------------\n")
    print(f"-------------------------------------------------\n")