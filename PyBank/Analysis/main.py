import os
import csv

budget_datafile = os.path.join ('..' , 'Resources' , 'budget_data.csv')

months = []
count_month = 0
total_profit_loss_change = []
net_profit_loss = 0
profit_loss_change = 0
previous_month_loss = 0
current_month_loss = 0

with open (budget_datafile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        count_month +=1
        current_month_loss = int(row[1])
        net_profit_loss+=current_month_loss
        
        if (count_month ==1):
           previous_month_loss=current_month_loss            
           continue
        else:
            months.append(row[0])
            profit_loss_change = current_month_loss - previous_month_loss
            total_profit_loss_change.append(profit_loss_change)
            previous_month_loss = current_month_loss
    sum_profit_loss = sum(total_profit_loss_change)
    average_profit_loss = round(sum_profit_loss/(count_month - 1), 2)
    highest_change = max(total_profit_loss_change)
    lowest_change = min(total_profit_loss_change)
    highest_month_index = total_profit_loss_change.index(highest_change)
    lowest_month_index = total_profit_loss_change.index(lowest_change)
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

print("Financial Analysis")

print("-------------------------------------------------")

print(f"Total Months:  {count_month}")

print(f"Total:  ${net_profit_loss}")

print(f"Average Change:  ${average_profit_loss}")

print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")

print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

output_path = os.path.join("financial.txt")
with open(output_path, 'w') as csvfile:
    csvfile.write(f"Financial Analysis\n")

    csvfile.write(f"-------------------------------------------------\n")

    csvfile.write(f"Total Months:  {count_month}\n")

    csvfile.write(f"Total:  ${net_profit_loss}\n")

    csvfile.write(f"Average Change:  ${average_profit_loss}\n")

    csvfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")

    csvfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")





  














