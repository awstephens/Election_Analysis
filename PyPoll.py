# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Dependencies used
import csv
import os

##### Opening csv file
# Assign a variable for the file to load and the path.
file_to_load = 'C:/Users/awste/OneDrive/Documents/BootCamp_StudyFiles/Week3/Module/Election Analysis/election_results.csv'


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    headers = next(file_reader)
    print(headers)



# Print each row in the CSV file
#    for row in file_reader:
#        print(row)


#close the file
#txt_file.close()


#close the file
#txt_file.close()