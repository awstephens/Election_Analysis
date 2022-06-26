# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Dependencies used
import csv
import os

##### Declaring input and output files
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("data", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("results", "election_analysis.txt")

# Setting up key variables to be used (no magic numbers)

# Initialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options = []

#Empty Dictionary to hold candidates and vote count
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the total votes. Test to make sure it works
        # print(total_votes)

# Working on candidate name list
        #Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)
            #print(candidate_options)

            #Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0
            
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
#Iterating through the candidate list
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes)*100
    # Print the candidate name and percentage of votes
    #print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")



    #Print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning percent = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        #Printing winning candidate, vote count and percentage
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------")

print(winning_candidate_summary)



# Print each row in the CSV file
#    for row in file_reader:
#        print(row)


#close the file
#txt_file.close()


#close the file
#txt_file.close()