# Program Name: plot_utils
# Purpose: Read a file and parse by a delimiter, help to create a new data set

import matplotlib.pyplot as plt

import statistical_data_analysis_tool as sdat


# create a table for some statistical values
def statistical_table(data_set, ax, axis_labels):
    """
    Builds a table plot by using matplotlib library to show some statistical details


    Parameters
    ----------
    data_set : list
        data series to calculate statistical values.
        data_set length should be equal axis_labels length.
        e.g: [[1,2,3,4] , [4,3,2,1]]

    ax : .axes.SubplotBase, or another subclass of ~.axes.Axes
        could be plot or sub_plot which is created before

    axis_labels : list
        specify column labels on the table.
        axis_labels length should be equal data_set length.
        eg: ["X1","X2"]
    """
    # set position on the figure
    ax.set_position([0.56, 0.28, 0.4, 0.5])
    # create an empty list for table rows
    data = []
    # create a table and calculate statistical values for multiple data set
    # each item in data_set is a list
    # each item in data set is calculated and put to data.
    # data will be contains of list. each list in the data indicate columns of table
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

    # first cell in each row will be row label
    rows = ['mean', 'std', 'min', 'quartile1', 'median', 'quartile3', 'max']

    # Get some pastel shades for the colors
    rowColors = ["#C4EFFF" for i in range(7)]
    colColors = ["#68D6FF" for i in range(2)]

    # Add a table at the center of the axes
    table = ax.table(cellText=data,
                     rowLabels=rows,
                     rowColours=rowColors,
                     colLabels=axis_labels,
                     colColours=colColors,
                     loc='center')
    # set table font sizze
    table.set_fontsize(12)
    # scale table
    table.scale(1, 3)
    # only show table , no axis
    ax.axis('off')


# create a table for correlation
def correlation_table(data_x, data_y, ax):
    """
    Builds a table plot by using matplotlib library to show correlation details


    Parameters
    ----------
    data_x : list
        first data series to calculate correlation. e.g [1,2,3,4]

    data_y : list
        second data series to calculate correlation. e.g [4,3,2,1]

    ax : .axes.SubplotBase, or another subclass of ~.axes.Axes
        could be plot or sub_plot which is created before
    """
    # set position on the figure
    ax.set_position([0.52, 0.28, 0.4, 0.5])
    # create row, first cell "label" , second cell "pearson correlation"
    table_data = [
        ["Pearson Correlation", sdat.correlation_pearson(data_x, data_y)]
    ]
    # specify cell color
    colors = [["#C4EFFF", "w"]]
    # create table object
    table = ax.table(cellText=table_data, cellColours=colors, loc='top')
    # set font size
    table.set_fontsize(12)
    # scale the table
    table.scale(1, 3)
    # only show table , no axis
    ax.axis('off')


# build a violin style plot
def build_plot_violin(data, title, axis_labels, ylabel, showTable=False, saveFig=False, figsize=(12, 5)):
    """
    Builds a violin style plot by using matplotlib library


    Parameters
    ----------
    data : list
        numeric data series which is required for plot.
        data length should be equal axis_labels length
        if data series more than one, the data should be like this:
        [[1,2,3,4] , [4,3,2,1]]

    title : str
        title where is placed on top of the figure.

    axis_labels : list
        labels where is placed on x line.
        axis_labels length should be equal data length.
        eg: ["X1","X2"]

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
    # create 1 row 2 column grid and put the violin plot to first cell
    ax = fig.add_subplot(121)
    # calculate some statistical values to show data points on the plot
    quartile1 = [(lambda x: sdat.quartile_first(x))(x) for x in data]
    medians = [(lambda x: sdat.median(x))(x) for x in data]
    quartile3 = [(lambda x: sdat.quartile_third(x))(x) for x in data]
    inds = range(1, len(medians) + 1)
    # send the statistical values to plot
    ax.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
    ax.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)

    # put the title to top of the figure
    ax.set_title(title)
    # put the labels to "x line"
    ax.set_xticklabels(axis_labels)
    # put the label to "y line"
    ax.set_ylabel(ylabel)

    # set style for the plot
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(range(1, len(axis_labels) + 1))
    ax.set_xlim(0.25, len(axis_labels) + 0.75)

    # send the data to plot to create a violin style plot
    ax.violinplot(data)
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
    # put the title to top of the figure
    ax.set_title(title)
    # put the labels to "x line"
    ax.set_xticklabels(axis_labels)
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


# build a scatter style plot
def build_plot_scatter(data_x, data_y, title, showTable=False, saveFig=False, figsize=(12, 5)):
    """
    Builds a scatter style plot by using matplotlib library


    Parameters
    ----------
    data_x : list
        first numeric data series which will be compare. e.g [1,2,3,4]

    data_y : list
        second numeric data series which will be compare. e.g [1,2,3,4]

    title : str
        title where is placed on top of the figure.

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
    # create 1 row 2 column grid and put the scatter plot to first cell
    ax = fig.add_subplot(121)

    # Create an scatter plot
    # put the title to top of the figure
    ax.set_title(title)
    # send the data_x and data_y to plot to create a scatter style plot
    ax.scatter(data_x, data_y)
    # create a table if showTable is True
    if (showTable):
        # put the table plot to second cell
        tbl = fig.add_subplot(122)
        # create table plot
        correlation_table(data_x, data_y, tbl)
    # show plot
    plt.show()
    # save the plot to disk
    if (saveFig):
        # Save the figure
        fig.savefig('build_plot_scatter.png')
