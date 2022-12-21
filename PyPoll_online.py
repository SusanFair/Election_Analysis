# data from election_results
# Use CSV module - import dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter and candidate_options
total_votes = 0
candidate_options = []

# Declare dictionary
candidate_votes ={}

# Winning candidates and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Using the open()function to open election_results.csv as election_data
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        # Print the candidate name for each row
        candidate_name = row[2]

        # Add candidate name to the candidate list.
        # If the candidate does not match any existing candidates add to list
        if candidate_name not in candidate_options:
            # Add candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Determine the percentage of votes per candidate
    for candidate_name in candidate_votes:

        # Vote count per candidate
        votes = candidate_votes[candidate_name]

        #Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Declare results variable
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #Print candidate's name and percentage of votes to the terminal
        print(candidate_results)
        # Save the cadidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # If votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #True set as winning_count and winning_percent
            winning_count = votes
            winning_percentage = vote_percentage
            # Set candidate as the winning candidate 
            winning_candidate = candidate_name


    # Print winning summary
    winning_candidate_summary = (
        f"------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winnning Vote Count: {winning_count:,}\n"
        F"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------------------\n")

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

    # commented out  print, print to file instead
    #print(winning_candidate_summary)




    # Print total votes
    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)








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