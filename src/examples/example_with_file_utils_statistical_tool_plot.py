# Program Name: plot_utils
# Purpose: Example of using plot_utils and file_utils libraries

import sys
from pathlib import Path

sys.path.append('./../')

from file_utils import read_csv, select_columns, get_columns, filter_by, group_by, create_data_series, sample_rows
from plot_utils import build_plot_violin, build_plot_box, build_plot_scatter


# create a data_set for box and violin style plot and show the plot
def box_violin_plot(data_set):
    """
    create a data_set for box and violin style plot and show the plot
    by using file_utils and plot_utils libraries


    Parameters
    ----------
    data_set : list
        data set will be used to create data series.
        eg : [{"Name":"test", "LastName":"test"}]
    """
    # not all data, get only  data of specified columns
    data_set = select_columns(data_set, ['NOC', 'Year', 'Medal'])
    # show a sample row
    print(f"Sample Row with only selected columns : {sample_rows(data_set, 1)}")
    print()

    # filter the data_set by 'CHN', 'GER' on "NOC" column and 'Silver', 'Bronze', 'Gold' on "Medal" columns
    data_set = filter_by(data_set, {"NOC": ['CHN', 'GER'], "Medal": ['Silver', 'Bronze', 'Gold']})
    # show a sample row
    print(f"Sample row with filter by :{sample_rows(data_set, 1)}")
    print()

    # group the data set by "NOC", "Year" columns and show only "NOC", "Year" columns and "count" aggregation result
    data_set = group_by(data_set, group_columns=["NOC", "Year"], show_columns=["NOC", "Year"], aggregation="count")
    # show a sample row
    print(f"Sample row with group_by :{sample_rows(data_set, 1)}")
    print()

    # create a data set
    data_set_plot = create_data_series(data_set, "NOC", "count_NOC_Year")
    # show the result
    print(f"create data set :{data_set_plot}")
    print()

    # design the result for plot
    data = [item[key] for item in data_set_plot for key in item]
    axis_labels = [key.replace('"', '') for item in data_set_plot for key in item]

    # build and show plot violin
    build_plot_violin(data, title="Compare Germany vs China", showTable=True, axis_labels=axis_labels, ylabel="Medals",
                      saveFig=True);

    # build and show plot box
    build_plot_box(data, title="Compare Germany vs China", showTable=True, axis_labels=axis_labels, ylabel="Medals",
                   saveFig=True);


# create a data_set for scatter style plot and show the plot
def scatter_plot(data_set):
    """
    create a data_set for scatter style plot and show the plot
    by using file_utils and plot_utils libraries


    Parameters
    ----------
    data_set : list
        data set will be used to create data series.
        eg : [{"Name":"test", "LastName":"test"}]
    """
    # scatter plot helps to display negative or positive correlation
    # Just one German athlete has been picked up to display correlation values
    print("Andrea Henkel is a retired German professional biathlete")

    # filter the data_Set by name
    data_set = filter_by(data_set, {"Name": ['Andrea Henkel (-Burke)']})
    # show a sample row
    print(f"Sample row with filter by :{sample_rows(data_set, 1)}")
    print()

    # not all data, get only  data of specified columns
    data_set = select_columns(data_set, ['Year', 'Medal'])
    # show a sample row
    print(f"Sample Row with only selected columns : {sample_rows(data_set, 1)}")
    print()

    # create a dat set with year like [2010,2012,2014]
    data_x = [int(item[key]) for item in data_set for key in item if key == 'Year']

    # create an empty list
    data_y = []
    # identify scale factor for Medals to determine the correlation between year vs medal
    # Gold:3 , Silver:2, Bronze:1
    for item in data_set:
        for key in item:
            if key == 'Medal':
                if item[key] == 'Gold':
                    data_y.append(3)
                elif item[key] == 'Silver':
                    data_y.append(2)
                elif item[key] == 'Bronze':
                    data_y.append(1)
                else:
                    data_y.append(0)
    # display data set
    print(f"data_x : {data_x}")
    print(f"data_x : {data_y}")

    # build and show plot scatter
    build_plot_scatter(data_x=data_x, data_y=data_y, title="Andrea Henkel Correlation", showTable=True, saveFig=True);


# read the file and get data set
data_folder = Path("data/")

file_to_open = data_folder / "athlete_events.csv"

data_set = read_csv(
    file_to_open,
    delimiter=";",
    clean_chars_header=['"']
)

# display a sample row
print()
print(f"Sample Row : {sample_rows(data_set, 1)}")

# display a columns of data_set which was created by read_csv
print()
columns = get_columns(data_set)
print(f"Columns : {columns}")

# test box and violin plot
box_violin_plot(data_set)

# test scatter plot
scatter_plot(data_set)
