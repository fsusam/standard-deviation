# Program Name: section06_example04_boxplot.py
# Purpose: To plot the fires per month in Brazil
# Example of: matplotlib boxplot
import matplotlib.pyplot as plt

from calc_functions import calc_median

# create an empty list for the data
fires_list = []

# read the data from the file
with open("amazon2.csv") as datafile:
    # for each line in the file
    for line in datafile:
        # split the line into the components
        year, state, month, fires, date = line.strip().split(",")
        
        # insert into the list
        fires_list.append(int(fires))
        
# create a figure and an axis object
fig, ax = plt.subplots()

# set the labels on the axes
ax.set_ylabel("Number of Fires per month")
# set the title
ax.set_title("Fires in Brazil 1998-2017")

# do a box plot
ax.boxplot(fires_list,showfliers=False)
plt.show() # display 

# save the image
fig.savefig('fires_boxplot.png', bbox_inches='tight')

print(f"Number of values: {len(fires_list)}")

# sort the list
print(f"Median is: {calc_median(fires_list)}")

mid_index = int(len(fires_list)/2)

print(f"Lower Quartile is: {calc_median(fires_list[:mid_index+1])}")
print(f"Upper Quartile is: {calc_median(fires_list[mid_index+1:])}")


