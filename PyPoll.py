# data from election_results
# Use CSV module - import dependencies
import csv
import os

# Assign a variable for the file to load and the path
# relative path: 
# file_to_load = "Resources/election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
    #election_data = open(file_to_load, 'r') or use with statement
#with open(file_to_load) as election_data:
#    print(election_data)


# Assign variable to save the file to a path
#Create a filename variable to a direct or indirect path to a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the open()function with the "W" mode open and read file
with open(file_to_load) as election_data:

#To Do: read and analyze the data here
# Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

#Print each row in the CSV file
   for row in file_reader:
    print(row)







#Test write to file & Close file
 #   txt_file.write("Counties in the Election\n")
 #   txt_file.write("-------------------------\n")
 #   txt_file.write("Arapahoe, ")
 #   txt_file.write("\nDenver, ")
 #   txt_file.write("\nJefferson")
 #   txt_file.write("\nKent, Lampton, Harwich")
#outfile.close()

# Close the file
#election_data.close()

# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote