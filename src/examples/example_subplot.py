import matplotlib.pyplot as plt 
import numpy as np

# Data for plotting
t = np.arange(0.01, 20.0, 0.01)

fig = plt.figure()

ax = plt.subplot(121)
ax1 = plt.subplot(122)
plt.subplots_adjust(left=0.5, right=2, top=0.9, bottom=0.1)

# Create a figure with 2 rows and 2 cols of subplots



# linear x and y axis
ax.plot(t, np.exp(-t / 5.0))
ax.set_title('linear x and y')
ax1.margins(1) 
ax.grid()


data = [[66386,12], [58230,333], [381139,4444],  [78045,0],  [99308,444]]

columns = ('Freeze','Test')
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]

# Get some pastel shades for the colors
colors = ["#C4EFFF" for i in range(5)]
colColors = ["#68D6FF" for i in range(2)]

# Add a table at the bottom of the axes
table = ax1.table(cellText=data,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      colColours=colColors,
                      loc='center')
table.set_fontsize(10)
table.scale(1,3)
ax1.axis('off')


#fig.tight_layout()
plt.show()



