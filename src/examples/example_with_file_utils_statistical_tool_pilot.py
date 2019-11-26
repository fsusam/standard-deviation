import sys

sys.path.append('./../')

from file_utils import read_csv, select_columns, get_columns, filter_by, group_by, create_data_set, sample_rows
from pilot_utils import build_pilot_violin, build_pilot_box, build_pilot_scatter

def box_violin_plot(data_set):
    data_set = select_columns(data_set, ['NOC', 'Year', 'Medal'] )
    print()
    print(f"Sample Row with only selected columns : {sample_rows(data_set,1)}" )
    
    
    print()
    data_set = filter_by(data_set, {"NOC":['CHN','GER'] , "Medal":['Silver','Bronze','Gold']} )
    print(f"Sample row with filter by :{sample_rows(data_set,1)}")
    
    print()
    data_set = group_by(data_set, group_columns=["NOC", "Year"] , show_columns=["NOC", "Year"], aggregation="count")
    print(f"Sample row with group_by :{sample_rows(data_set,1)}")
    
    print()
    data_set_plot = create_data_set(data_set, "NOC", "count_NOC_Year")
    print(f"create data set :{data_set_plot}")
    
    # create data set for plot
    data = [ item[key] for item in data_set_plot for key in item]
    axis_labels = [key.replace('"', '') for item in data_set_plot for key in item]
    
    # build and show pilot violin
    build_pilot_violin(data, title="Compare Germany vs China", showTable=True, axis_labels=axis_labels, ylabel="Medals", saveFig=True);
    
    # build and show pilot box
    build_pilot_box(data, title="Compare Germany vs China",showTable=True, axis_labels=axis_labels, ylabel="Medals", saveFig=True);
    
def scatter_plot(data_set):
    print("Andrea Henkel is a retired German professional biathlete")
    data_set = filter_by(data_set, {"Name":['Andrea Henkel (-Burke)']} )
    print(f"Sample row with filter by :{sample_rows(data_set,1)}")
    
    data_set = select_columns(data_set, ['Year', 'Medal'] )
    print()
    print(f"Sample Row with only selected columns : {sample_rows(data_set,1)}" )
    
    data_x = [int(item[key]) for item in data_set for key in item if key=='Year']
    
    data_y = []
    for item in data_set:
        for key in item:
            if key=='Medal':
                if item[key]=='Gold':
                    data_y.append(3)
                elif item[key]=='Silver':
                    data_y.append(2)
                elif item[key]=='Bronze':
                    data_y.append(1)
                else:
                    data_y.append(0)

    print(f"data_x : {data_x}")
    print(f"data_x : {data_y}")
    
    build_pilot_scatter(data_x=data_x, data_y=data_y, title="Andrea Henkel Correlation",showTable=True, saveFig=True);    
    
data_set = read_csv(
        "/home/fsusam/Development/workspace/python/standard-deviation/src/examples/data/athlete_events.csv",
        delimiter=";",
        clean_chars_header=['"']
        )

print()
print(f"Sample Row : {sample_rows(data_set,1)}" )

print()
columns = get_columns(data_set)
print(f"Columns : {columns}")

# test box and violin plot
box_violin_plot(data_set)

# test scatter plot
scatter_plot(data_set)