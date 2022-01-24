# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # Print the file object.
     # print(election_data)



# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

    # Write three counties to the file. 
    # txt_file.write("Counties in the Election\n_________________________\nArapahoe\nDenver\nJefferson")

#To do: read and analyze the date here. 
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

 # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)        
    