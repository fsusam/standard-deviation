import matplotlib.pyplot as plt 
fig = plt.figure(dpi=80)
ax = fig.add_subplot(1,1,1)
table_data=[[10]]
rows = ["Pearson Correlation"]
rowColors = ["#C4EFFF"]

table = ax.table(cellText=table_data, rowLabels=rows, rowColours=rowColors, loc='center')
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')
plt.show()