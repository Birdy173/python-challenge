#import libraries to read csv files across operating systems
import os
import csv

#open budget_data.csv
budget_csv = os.path.join("Resources", "budget_data.csv")

#initializes variables used throughout the code
total_months = 0 
net_total = 0
changes = []
average_change = 0
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

#reads csv files using the csv module
with open(budget_csv) as csv_file:

    #csv reader that specifies the delimiter
    csv_reader = csv.reader(csv_file, delimiter= ",")

    #skips the header for the calculations
    csv_header = next(csv_reader)

    #start looping through all the rows of the csv file
    for row in csv_reader:
        #update the total number of months for each row
        total_months += 1
        
        #grabs the profit/losses row and calulates the net_total since losses have - signs
        current_profit_losses = int(row[1])
        net_total += int(row[1])
        
        #calculates the change from the previous month
        if total_months > 1:
            change = current_profit_losses- previous_profit_losses
            changes.append(change)

            #checks for the greatest increase and updates the dictionary
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = change
            
            #checks for the greatest decrease and updates the dictionary
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = change

        #updates previous_profit_losses
        previous_profit_losses = current_profit_losses

#calulates the average change and avoids dividing by zero
if len(changes) != 0:
    average_change = round(sum(changes)/len(changes), 2)

#creates a function to print out results to console
def print_results_console():
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})')
    print(f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})')
print_results_console()

#creates a function to output the text file
def output_txt():
    #opens the file in write mode instead of read mode
    output_csv = os.path.join("analysis", "financial_analysis.txt")

    #writes out the rows of the file using the calculations
    with open(output_csv, "w") as textfile:
        csv_writer = csv.writer(textfile) 
        csv_writer.writerow(["Financial Analysis"])
        csv_writer.writerow(["----------------------------"])
        csv_writer.writerow([f'Total Months: {total_months}'])
        csv_writer.writerow([f'Total: ${net_total}'])
        csv_writer.writerow([f'Average Change: ${average_change}'])
        csv_writer.writerow([f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})'])
        csv_writer.writerow([f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})'])
output_txt()


        
