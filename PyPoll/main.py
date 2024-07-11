#import libraries that allow us to read csv files across operating systems
import os 
import csv

#opens election_data.csv
election_data_csv = os.path.join("Resources", "election_data.csv")

#initializes all variables used throughout the code
total_votes = 0
candidates = {}
candidate_results = []
max_votes = 0
winner = ""

#open and read csv
with open(election_data_csv) as cvs_file:
    #cvs reader that specifies the delimiter
    csv_reader = csv.reader(cvs_file, delimiter = ",")
    
    #skips the header for calculations
    cvs_header = next(csv_reader)
    
    #starts looping through each of the rows of the csv file
    for row in csv_reader:
        #calculates the number of votes based on how many rows excluding header
        total_votes += 1

        #gets the candidate name from column 3
        candidate_name = row[2]

        #states if the candidate is already in the dictionary, increase their vote by 1
        if candidate_name in candidates:
            candidates[candidate_name] += 1

        #otherwise it starts their vote at 1
        else:
            candidates[candidate_name] = 1

    #calculates the percentage and votes
    for candidate, votes in candidates.items():
        percentage = round((votes/total_votes)*100, 3)
        candidate_results.append((candidate, votes, percentage))
        
        #finds out what candidate has the max number of votes 
        if votes > max_votes:
            max_votes = votes
            winner = candidate


#creates function to print results to the console
def print_results_console():
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")
    for candidate, votes, percentage in candidate_results:
        print(f'{candidate}: {percentage}% ({votes})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
print_results_console()

#creates a function to print results to a text file
def output_txt():
    #opens the file in write mode instead of read mode
    output_csv = os.path.join("analysis", "election_results.txt")

    #writes out the rows of the file based on the calculations above
    with open(output_csv, "w") as textfile:
        csv_writer = csv.writer(textfile)
        csv_writer.writerow(["Election Results"])
        csv_writer.writerow(["-------------------------"])
        csv_writer.writerow([f'Total Votes: {total_votes}'])
        csv_writer.writerow(["-------------------------"])
        for candidate, votes, percentage in candidate_results:
            csv_writer.writerow([f'{candidate}: {percentage}% ({votes})'])
        csv_writer.writerow(["-------------------------"])
        csv_writer.writerow([f'Winner: {winner}'])
        csv_writer.writerow(["-------------------------"])
output_txt()