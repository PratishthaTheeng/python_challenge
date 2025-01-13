# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_profit_loss = 0
net_changes = []
greatest_increase = {"month": "", "amount": float("-inf")}
greatest_decrease = {"month": "", "amount": float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

       # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1  # Increment for the first month
    first_month_profit_loss = int(first_row[1])  # First month profit/loss
    previous_profit_loss = first_month_profit_loss  # Set the first month profit/loss as reference

    # Track the total and net change
    total_net += first_month_profit_loss  # Add the first month's profit/losscd
    # Process each row of data
    for row in reader:
        
        month = row[0]
        profit_or_loss = int(row[1])

        # Track the total months and total net profit/loss
        total_months += 1
        total_net += profit_or_loss

        # Track the net change
        net_change = profit_or_loss - previous_profit_loss
        net_changes.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase["amount"]:
            greatest_increase["amount"] = net_change
            greatest_increase["month"] = month

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease["amount"]:
            greatest_decrease["amount"] = net_change
            greatest_decrease["month"] = month

        # Update previous_net to the current row's profit/loss
        previous_profit_loss = profit_or_loss

# Calculate the average net change across the months
average_change = sum(net_changes) / len(net_changes) if net_changes else 0

# Generate the output summary
output = f'''
Financial Analysis
-------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase["month"]} (${greatest_increase["amount"]})
Greatest Decrease in Profits: {greatest_decrease["month"]} (${greatest_decrease["amount"]})
'''

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
