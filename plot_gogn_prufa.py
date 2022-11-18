import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


dataframes = []

# read all csv files in the folder gogn and append them to a list
for filename in os.listdir('gogn'):
    df = pd.read_csv(f'gogn/{filename}')
    dataframes.append(df)

close_list = []
# get values in column 'Close' and 'date' from all dataframes and append them to a list
for df in dataframes:
    close_list.append(df[['Symbol','Close', 'Date']])
    
print(close_list[1].head())


# bara ad testa, bara taka gildin thar sem dagsetningin er eins
# sumar rafmyntir komu langt a eftir t.d. bitcoin

# only keep the rows where all dates are the same
# this is a bit tricky, but you can do it with the following code
# first we create a list of all the dates
dates = []
for df in close_list:
    dates.append(df['Date'].tolist())
# then we find the intersection of all the dates
# (the dates that are in all the lists)
dates = list(set.intersection(*map(set, dates)))
# then we filter the dataframes so that only rows with these dates remain
for i in range(len(close_list)):
    close_list[i] = close_list[i][close_list[i]['Date'].isin(dates)]
   
   

print(close_list[1].head()) 
print(close_list[1].tail())
# make all indexes start from 0
for i in range(len(close_list)):
    close_list[i] = close_list[i].reset_index(drop=True)


percent_change = []
# calculate the percent change for each dataframe along with the date and symbol
for df in close_list:
    percent_change.append(df['Close'].pct_change())

# replace with cumulative sum of percent change
for i in range(len(percent_change)):
    percent_change[i] = percent_change[i].cumsum()

for df in percent_change:
    plt.plot(df)

plt.show()
