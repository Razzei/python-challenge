import csv

path = "Resources/budget_data.csv"

with open(path) as csvfile:
    csvreader = csv.reader(csvfile)

    # Get rid of header
    csvheader = next(csvreader)

    # Count number of months and total profit/loss in the file
    num_month = 0
    total = 0
    profit_loss = []

    for row in csvreader:
        num_month = num_month + 1
        total = total + int(row[1])
        profit_loss.append(int(row[1]))

    # Count average change
    change = 0
    initial = 867884
    increase_decrease = []
    for i in profit_loss:

        if initial != i:
            increase_decrease.append(i - initial)
            change = change + (i - initial)
            initial = i
    avg_change = change/(num_month-1)

    # Greatest increase/decrease
    increase = max(increase_decrease)
    decrease = min(increase_decrease)

# Analysis
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {num_month}")
print(f"Total: {total}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: ${increase}")
print(f"Greatest Increase in Profits: ${decrease}")

output_path = "analysis/analysis.txt"
with open(output_path, 'w') as f:
    f.write("Financial Analysis")
    f.write('\n')
    f.write("--------------------------------")
    f.write('\n')
    f.write(f"Total Months: {num_month}")
    f.write('\n')
    f.write(f"Total: {total}")
    f.write('\n')
    f.write(f"Average Change: ${round(avg_change, 2)}")
    f.write('\n')
    f.write(f"Greatest Increase in Profits: ${increase}")
    f.write('\n')
    f.write(f"Greatest Increase in Profits: ${decrease}")