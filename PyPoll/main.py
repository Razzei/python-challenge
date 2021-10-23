import csv
from types import ClassMethodDescriptorType

path = "Resources/election_data.csv"

with open(path) as csvfile:
    csvreader = csv.reader(csvfile)

    # Get rid of header
    csvheader = next(csvreader)

    # Total votes
    total = 0
    khan = 0
    correy = 0
    li = 0
    tooley = 0
    for row in csvreader:
        total = total + 1
        if row[2] == "Khan":
            khan = khan + 1
        elif row[2] == "Correy":
            correy = correy + 1
        elif row[2] == "Li":
            li = li + 1
        elif row[2] == "O'Tooley":
            tooley = tooley + 1
    
    # Who won
    talley = [khan, correy, li, tooley]
    vote = 0
    max = max(talley)
    if max == khan:
        winner = "Khan"
    elif max == correy:
        winner = "Correy"
    elif max == li:
        winner = "Li"
    elif max == tooley:
        winner = "O'Tooley"

    #Percent of votes
    khan_percent = round(talley[0]/total * 100)
    correy_percent = round(talley[1]/total * 100)
    li_percent = round(talley[2]/total * 100)
    tooley_percent = round(talley[3]/total * 100)

    # Analysis
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total}")
    print("----------------------------")
    print(f"Khan: {khan_percent}% ({khan})")
    print(f"Correy: {correy_percent}% ({correy})")
    print(f"Li: {li_percent}% ({li})")
    print(f"O'Tooley: {tooley_percent}% ({tooley})")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

output_path = "analysis/analysis.txt"
with open(output_path, 'w') as f:
    f.write("Election Results")
    f.write('\n')
    f.write("--------------------------------")
    f.write('\n')
    f.write(f"Total Votes: {total}")
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')
    f.write(f"Khan: {khan_percent}% ({khan})")
    f.write('\n')
    f.write(f"Correy: {correy_percent}% ({correy})")
    f.write('\n')
    f.write(f"Li: {li_percent}% ({li})")
    f.write('\n')
    f.write(f"O'Tooley: {tooley_percent}% ({tooley})")
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')
    f.write(f"Winner: {winner}")
    f.write('\n')
    f.write("----------------------------")
