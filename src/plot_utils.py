# Program Name: plot_utils
# Purpose: Read a file and parse by a delimiter, help to create a new data set

import matplotlib.pyplot as plt

import statistical_data_analysis_tool as sdat


def set_axis_style(ax, labels, xlabel=None):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(range(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    if (xlabel):
        ax.set_xlabel(xlabel)


def violin(data, ax, title, inds, medians, quartile1, quartile3, ylabel, axis_labels):
    ax.set_title(title)
    ax.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
    ax.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
    ax.set_ylabel(ylabel)
    ax.violinplot(data)
    # set style for the axes
    set_axis_style(ax, axis_labels)


def scatter(data_x, data_y, ax, title):
    ax.set_title(title)
    ax.scatter(data_x, data_y)


def statistical_table(data_set, ax, axis_labels):
    # table
    # data = [[66386,12], [58230,333], [381139,4444],  [78045,0],  [99308,444],[99308,444],[99308,444]]
    ax.set_position([0.56, 0.28, 0.4, 0.5])
    data = []

    for item in data_set:
        if (len(data) == 0):
            data = [
                [sdat.mean(item)],
                [sdat.standard_deviation(item)],
                [sdat.min_data_set(item)],
                [sdat.quartile_first(item)],
                [sdat.median(item)],
                [sdat.quartile_third(item)],
                [sdat.max_data_set(item)],
            ]
        else:
            for idx, cell in enumerate(data):
                if (idx == 0):
                    cell.append(sdat.mean(item))
                if (idx == 1):
                    cell.append(sdat.standard_deviation(item))
                if (idx == 2):
                    cell.append(sdat.min_data_set(item))
                if (idx == 3):
                    cell.append(sdat.quartile_first(item))
                if (idx == 4):
                    cell.append(sdat.median(item))
                if (idx == 5):
                    cell.append(sdat.quartile_third(item))
                if (idx == 6):
                    cell.append(sdat.max_data_set(item))

    rows = ['mean', 'std', 'min', 'quartile1', 'median', 'quartile3', 'max']

    # Get some pastel shades for the colors
    rowColors = ["#C4EFFF" for i in range(7)]
    colColors = ["#68D6FF" for i in range(2)]

    # Add a table at the bottom of the axes
    table = ax.table(cellText=data,
                     rowLabels=rows,
                     rowColours=rowColors,
                     colLabels=axis_labels,
                     colColours=colColors,
                     loc='center')
    table.set_fontsize(12)
    table.scale(1, 3)
    ax.axis('off')


def correlation_table(data_x, data_y, ax):
    ax.set_position([0.52, 0.28, 0.4, 0.5])
    table_data = [
        ["Pearson Correlation", sdat.correlation_pearson(data_x, data_y)]
    ]

    colors = [["#C4EFFF", "w"]]
    table = ax.table(cellText=table_data, cellColours=colors, loc='top')
    table.set_fontsize(12)
    table.scale(1, 3)
    ax.axis('off')


def build_plot_violin(data, title, axis_labels, ylabel, showTable=False, saveFig=False, figsize=(12, 5)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(121)

    quartile1 = [(lambda x: sdat.quartile_first(x))(x) for x in data]
    medians = [(lambda x: sdat.median(x))(x) for x in data]
    quartile3 = [(lambda x: sdat.quartile_third(x))(x) for x in data]
    inds = range(1, len(medians) + 1)

    violin(data, ax, title, inds, medians, quartile1, quartile3, ylabel, axis_labels)

    if (showTable):
        tbl = fig.add_subplot(122)
        statistical_table(data, tbl, axis_labels)

    plt.show()

    if (saveFig):
        # Save the figure
        fig.savefig('build_plot_violin.png', bbox_inches='tight')


# build a box style plot
def build_plot_box(data, title, axis_labels, ylabel, showTable=False, saveFig=False, figsize=(12, 5)):
    """
    Builds a box style plot by using matplotlib library


    Parameters
    ----------
    data : list
        numeric data series which is required for plot. e.g [1,2,3,4]

    title : str
        title where is placed on top of the figure.

    axis_labels : list
        labels where is placed on x line

    ylabel : str
        labels where is placed on x line

    showTable : bool
        table where is next to plot to show some statistical values such as "std, mean, median etc..."
        Default is False

    saveFig: bool
        Save the result plot to disk as image. Default is False

    figsize: tuple
        figure size. Default is (12,5)
    """
    # create figure object
    fig = plt.figure(figsize=figsize)
    # create 1 row 2 column grid and put the box plot to first cell
    ax = fig.add_subplot(121)
    # Create an box plot
    # put the labels to "x line"
    ax.set_xticklabels(axis_labels)
    # put the title to top of the figure
    ax.set_title(title)
    # put the label to "y line"
    ax.set_ylabel(ylabel)
    # send the data to plot to create a box style plot
    ax.boxplot(data)
    # create a table if showTable is True
    if (showTable):
        # put the table plot to second cell
        tbl = fig.add_subplot(122)
        # create table plot
        statistical_table(data, tbl, axis_labels)
    # show plot
    plt.show()
    # save the plot to disk
    if (saveFig):
        # Save the figure
        fig.savefig('build_plot_box.png', bbox_inches='tight')


def build_plot_scatter(data_x, data_y, title, showTable=False, saveFig=False, figsize=(12, 5)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(121)

    # Create an scatter plot   
    scatter(data_x, data_y, ax, title)

    if (showTable):
        tbl = fig.add_subplot(122)
        correlation_table(data_x, data_y, tbl)

    plt.show()

    if (saveFig):
        # Save the figure
        fig.savefig('build_plot_scatter.png')
