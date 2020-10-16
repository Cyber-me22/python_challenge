# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:08:03 2020

@author: mahdi
"""
import os
import csv

file_to_load = "Resources/budget_data.csv"
file_to_output = "Analysis/budget_analysis.txt"
total_months = 0 
total_net = 0 
greatest_increase = 0
greatest_decrease = 0
net_change_list = [] 
month_of_change = "" 
#Open the CSV 
with open(file_to_load) as financial_data:
     reader = csv.reader(financial_data)
     # Read the header row
     header = next(reader)
#     # Extract first row to avoid appending to net_change_list
     first_row = next(reader)
     total_months += 1
     total_net += int(first_row[1])
     prev_net = int(first_row[1])
     for row in reader:
        # Track the total
        total_months += 1
        total_net += int(row[1])
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change = row[0]
        # Calculate the greatest increase
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = month_of_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = month_of_change
            
Average = round(sum(net_change_list) / len(net_change_list),2)

output = (f'total of months {total_months}\ntotal net {total_net}\naverage {Average}\ngreatest increase {greatest_increase}\ngreatest decrease {greatest_decrease}\ngreatest decrease month {greatest_decrease_month}\ngreatest increase month {greatest_increase_month}')
print(output)

file_to_output = "Analysis/budget_analysis.txt"
with open(file_to_output, 'w', newline='') as datafile:
    datafile.write(output)
    
     
     
