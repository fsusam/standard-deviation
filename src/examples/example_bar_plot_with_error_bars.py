import matplotlib.pyplot as plt

import sys

sys.path.append('./../')

from statistical_data_analysis_tool import mean, standard_deviation

# Enter raw data
year_2017 = [1000,10,10,12,10,9,10,10,12,10,10,10]
year_2018 = [0,0,0,0,2,0,0,0]
year_2019 = [1,5,0,2,0,4,10,0,3,0,0,1]

# Calculate the average
year_2017_mean = mean(year_2017)
year_2018_mean = mean(year_2018)
year_2019_mean = mean(year_2019)

# Calculate the standard deviation
year_2017_std = standard_deviation(year_2017)
year_2018_std = standard_deviation(year_2018)
year_2019_std = standard_deviation(year_2019)


# Create lists for the plot
years = ['2017', '2018', '2019']
x_pos = range(len(years))
CTEs = [year_2017_mean, year_2018_mean, year_2019_mean]
error = [year_2017_std, year_2018_std, year_2019_std]

# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(years)
ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()



