# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}

# Winning Candidate and Winning Count Tracker
winner = ""
max_votes = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
       
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
         candidates[candidate_name] = 1
        # Add a vote to the candidate's count
        else:
         candidates[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    line_dash = "------------------"
    print("\nElection Results")
    print(line_dash)
    txt_file.write("Election Results")
    txt_file.write("\n"+line_dash)

    # Print the total vote count (to terminal)
    output = f"Total Votes: {total_votes}"
    print(output)
    print(line_dash)

    # Write the total vote count to the text file
    txt_file.write("\n"+output)
    txt_file.write("\n"+line_dash)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate,votes in candidates.items():
        # Get the vote count and calculate the percentage
        total_candidate_vote_percentage = (votes/total_votes)*100

        # Update the winning candidate if this one has more votes
        if votes > max_votes:
           max_votes = votes
           winner = candidate
        # Print and save each candidate's vote count and percentage
        output = f"{candidate}: {total_candidate_vote_percentage:.3f}% ({votes})"
        print(output)
        txt_file.write("\n"+output)
     
    # Generate and print the winning candidate summary
    output = f"Winner: {winner}"
    print(line_dash)
    print(output)
    print(line_dash)
    txt_file.write("\n"+line_dash)

    # Save the winning candidate summary to the text file
    txt_file.write("\n"+output)
    txt_file.write("\n"+line_dash)