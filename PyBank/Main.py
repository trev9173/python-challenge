def main():


import pandas as pd
import os
import csv


budget_data_df = pd.read_csv(budget_data, encoding="ISO-8859-1")
budget_data_df_noHead = pd.read_csv(budget_data, encoding="ISO-8859-1", skiprows=1, header=None)
budget_data_df
budget_data_df_noHead

revenue_sum = budget_data_df["Revenue"].sum()

num_of_months = len(budget_data_df_noHead)

# list of the changes
import csv

RevenueChanges = []
Revenue = 0
Change = 0

with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader, None)

    for row in csv_reader:
        Change = (int(row[1]) - int(Revenue))
        RevenueChanges.append(Change)

        Revenue = int(row[1])


budget_data_df["Year to Year Revenue Change"] = RevenueChanges

average_change = budget_data_df["Year to Year Revenue Change"].mean()

max_change = budget_data_df["Year to Year Revenue Change"].max()

min_change = budget_data_df["Year to Year Revenue Change"].min()

max_change_month = (budget_data_df.loc[budget_data_df["Year to Year Revenue Change"] == max_change, ['Date']].values[0])
min_change_month = (budget_data_df.loc[budget_data_df["Year to Year Revenue Change"] == min_change, ['Date']].values[0])

print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(num_of_months))
print("Total Revenue: $" + str(revenue_sum))
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Revenue:  " + str(max_change_month) + " $" + str(max_change))
print("Greatest Decrease in Revenue:  " + str(min_change_month) + " $" + str(min_change))

main()