import matplotlib.pyplot as plt
import numpy as np


def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3
    lower_adjacent_value = q1
    return lower_adjacent_value, upper_adjacent_value


def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample name')


# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
inds = range(1, len(medians) + 1)

fig, ax1 = plt.subplots()

ax1.set_title('Default violin plot')
ax1.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax1.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax1.set_ylabel('Observed values')
ax1.violinplot(data)

# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax1, labels)

plt.subplots_adjust(bottom=0.15, wspace=0.05)
plt.show()