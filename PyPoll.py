# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Add total_votes counter
total_votes = 0

# Candidate Options
candidate_options =[]

# Candidate number of votes dictionary
candidate_votes = {}

# Winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Write three counties to the file. 
    # txt_file.write("Counties in the Election\n_________________________\nArapahoe\nDenver\nJefferson")
 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        #If candidate does not match any existing cadidate
        if candidate_name not in candidate_options:
            # Add candidate name to candidate list  
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

    #Save the results to text file
    with open(file_to_save, "w") as txt_file:

        #Write Election Results text
        election_result = (
            f"\nElection Results\n"
            f"_________________________\n"
            f"Total Votes: {total_votes:,}\n"
            f"_________________________\n")
        print(election_result, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_result)

        # Determine the percentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print the candidate name and percentage of votes.
            #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
            
            # To do: print out the winning candidate, vote count and percentage to the terminal.
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # To do: print election results to text file
            # Candidate's election results
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            # Write to text file
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)

