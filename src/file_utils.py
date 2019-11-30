# Program Name: file_utils
# Purpose: Read a file and parse by a delimiter, help to create a new data set

# Read CSV file line by line and split the lines into columns
def read_csv(path, delimiter=',', header=True, clean_chars_header=[]):
    """
    Read CSV file line by line and split the lines into columns.

    The delimiter is default "," but it can be specified a different char.
    "header" should be True if the file has header.

    If the file has any special char in header like '"' , this char can be removed if it is specified inside
    "clean_chars_header"

    Parameters
    ----------
    path : str
        absolute file path. eg: /home/user/workspace/data.csv

    delimiter : str
        splitter char for lines. Default is ","

    header : bool
        specify the file has a header. Default is "True"

    clean_chars_header : list
        it will be removed the chars inside list. Default is "empty list"

    Returns
    -------
    list
        return the dictionary list. eg [{"Name":"test", "LastName":"test"}]
    """
    # return list
    result = []
    # create empty list
    columns = []
    # flag to check the columns was created
    is_columns_created = False
    # it will be increment +1 if face any issue during splitting
    split_error_count = 0
    # Display a sample line which is faced an issue during splitting
    sample_split_error = ''

    # open the file
    with open(path) as datafile:
        # read the file line by line
        for line in datafile:
            # split the line by delimiter
            row = line.strip().split(delimiter)
            # check if the columns were created or not
            if (not is_columns_created):
                # create columns by using header if the file has a header
                if (header):
                    # create columns with header
                    columns = create_col(row, clean_chars=clean_chars_header)
                    # switch "true" if columns could be created properly
                    is_columns_created = True
                    # skip first line if it is header
                    continue
                else:
                    # create default columns if the file has not a header
                    columns = create_col(col_count=len(row), clean_chars=clean_chars_header)
                    # switch "true" if columns could be created properly
                    is_columns_created = True
            # the line was not split properly since it may have some the same delimiter char which is being used for
            # splitting inside the item
            if len(row) != len(columns):
                # increment the split error counter
                split_error_count += 1
                # assign the last failure line
                sample_split_error = line
            else:
                # create a empty dictionary row
                row_dict = {}
                # build dictionary with key:header_name, value: line_cell
                for idx, col_value in enumerate(row):
                    row_dict[columns[idx]] = col_value
                # append the dictionary to result list
                result.append(row_dict)
    # display the line which was split wrong to help fixing the issue for user
    # user may change delimiter or fix some cell
    if (split_error_count > 0):
        print(f"[{split_error_count}] rows could not be splitted. Sample row : [{sample_split_error}] ")
    # return result list which contains some dictionary items
    return result


# create a data set with only selected columns
def select_columns(data, cols):
    """
    Create a data set with only selected columns

    Parameters
    ----------
    data : list
        original data set. eg : [{"Name":"test", "LastName":"test"}]

    cols : list
        selected columns. eg : ["Name"]

    Returns
    -------
    list
        new data set which contains only selected columns. eg : [{"Name":"test"}]
    """
    # new data set which will be created with selected columns
    selected_columns_data_set = []
    # get values of selected columns from the data which is given as input paramater
    for row in data:
        # invoke the build_row_by_columns function to get the column value
        selected_columns_data_set.append(build_row_by_columns(row, cols))
    # return new data set which contains only selected columns
    return selected_columns_data_set


# build new dictionary which contains only selected columns
def build_row_by_columns(data_item, cols):
    """
    Build new dictionary which contains only selected columns

    Parameters
    ----------
    data_item : dict
        original item inside data set. eg : {"Name":"test", "LastName":"test"}

    cols : list
        selected columns. eg : ["Name"]

    Returns
    -------
    dict
        new dictionary which contains only selected columns eg : {"Name":"test"}
    """
    # do nothing if "cols" are empty or "None"
    if not cols:
           return data_item
    # create an empty dictionary
    row_dict = {}
    # use each column as a key for new dictionary object and the item where is inside the original dictionary assign
    # to key
    for select_col in cols:
        # the key is selected column, value is found inside the original dictionary by key
        row_dict[select_col] = data_item[select_col]
    # return new dictionary which contains only selected columns
    return row_dict


# return subset of list by specified count
def sample_rows(data, count=1):
    """
    return subset of list by specified count

    Parameters
    ----------
    data : list
        data set. eg : [{"Name":"test", "LastName":"test"} , {"Name":"test1", "LastName":"test1"}]

    count : int
        subset of list count. Default is 1

    Returns
    -------
    list
        subset of list eg : [{"Name":"test", "LastName":"test"}]
    """
    # return subset of list
    return data[:count]


# get columns of data set
def get_columns(data):
    """
    Each item of data set is consists of a dictionary type. The keys of the dictionary item indicate columns.
    One sample item in the data set is enough to get columns
    because each dictionary in the data set consists of the same structure.
    This function allows users to see columns and gets the data by using these columns.

    The data set must have at least one item.

    Parameters
    ----------
    data : list
        data set. eg : [{"Name":"test", "LastName":"test"} , {"Name":"test1", "LastName":"test1"}]

    Returns
    -------
    list
        columns of the data set : ["Name", "LastName"}]

    """
    return [item for item in data[0]]


# create column list by using header of file or create default columns
def create_col(header=None, col_count=None, clean_chars=[]):
    """
    Creates a unique column list by using the header of file or,
    build a list by creating the unique name if there is no existing header.

    "header" and "col_count" should not be assigned value at the same time.
    If it is assigned then "header" has more priority

    Parameters
    ----------
    header : list
        header of the file. Default is None. eg : ["Name","LastName"]

    col_count : int
        created a list which contains a unique name by col_count.
        eg: if count is 2 , function creates ["col_1", "col_2"]

    Returns
    -------
    list
        columns of the data set : ["Name", "LastName"}] or ["col_1", "col_2"]

    """
    # create an empty list
    col_names = []
    # use header if it is specified
    if (header):
        for col_name in header:
            # send each item in header to build unique column name
            col_names.append(create_column_name(col_names, col_name, clean_chars))
    elif (col_count):  # build unique default column names
        col_names = [f"col_{i + 1}" for i in range(col_count)]
    # return unique column name
    return col_names


# create a column name by using the value in the input parameter
def create_column_name(col_names, value, clean_chars):
    """
    Create a column name  by using the value in the input parameter.
    All whitespace chars and the char which was specified inside clean_chars are removed.
    If the value is existing inside the col_names, the value is made be unique by adding suffix. eg : "Name_1"

    Parameters
    ----------
    col_names : list
        list of the column names. eg : ["Name","LastName"]

    value : str
        column name. eg: "Name"

    clean_chars : list
        the list of chars which will be removed. eg: '"'

    Returns
    -------
    str
        column name. eg: "Name" or "Name_1"
    """
    # clean the char inside the value if specified any char in clean_chars list
    if value:
        for cc in clean_chars:
            # clean the char inside clean_chars and any all whitespace in the value
            value = ''.join(value.split()).replace(cc, '')
        else:  # clean all whitespace in the value
            value = ''.join(value.split())
    # col suffix index
    col_idx = 1
    # add the index as suffix and increment if after adding if the column name is existing in the list
    while True:
        if value in col_names:
            value = f"{value}_{col_idx}"
            col_idx += 1
        else:  # return the value after finish all process
            return value


# filter the data set by values
def filter_by(data, filter_values):
    """
    The data is given to the function to to filter by the values inside filter_values.
    The "filter" function is used to do that.

    Parameters
    ----------
    data : list
        consists of the dictionary items.
        eg : [{"Name":"test", "LastName":"test"} , {"Name":"test1", "LastName":"test1"}]

    filter_values : dict
         consists of the dictionary items. the key of the dictionary item corresponds to the key of the dictionary
         in the data. The data is filtered by values that are specified in filter_values.
        eg: {"Name":["test"]}

    Returns
    -------
    list
        filtered the data. eg: [{"Name":"test", "LastName":"test"}]
    """
    # assign the data to variable
    filtered_list = data
    # filter_values is consists of dictionary. The key in the dictionary  indicates to a key of the dictionary
    # in the data set. The value in the dictionary is used to filter the data set
    for filter_col in filter_values:
        filtered_list = list(filter(lambda data: data[filter_col] in filter_values[filter_col], filtered_list))
    # return the filtered list
    return filtered_list


# Group the data by specified columns and aggregate some columns by the aggregation method
def group_by(data, group_columns, aggregation, show_columns):
    """
    The data is given to the function to group by the values inside group_columns and aggregate the column which is
    specified inside group_columns by an aggregation method.

    The new data set which is created after the aggregation process consists of a new column that is created
    inside this function. This new column is named by merging items inside group_columns.
    eg : if the group_columns like ["Name"] , the group name column is named like "count_Name"

    Only the "count" aggregation method is supported for now.

    Parameters
    ----------
    data : list
        consists of the dictionary items.
        eg : [{"Name":"test", "LastName":"test"} , {"Name":"test", "LastName":"test1"}]

    group_columns : list
         consists of column names. eg: ["Name"]

    aggregation : str
        specified the aggregation method. eg: "count"

    show_columns : list
        specified the columns which will be inside the new data set. Default is "None". 
        eg: ["Name"]

    Returns
    -------
    list
        grouped the data set. eg: [{"Name":"test", "count_Name":2}]

    Raises
    ------
    Exception
        raise exception if one of input parameter is None or empty
        raise exception if items of show_columns are not in group_columns
        raise exception if the aggregation method is not supported
    """
    # raise exception if one of input parameter is None or empty
    if not all([data, group_columns, aggregation, show_columns]):
        raise Exception('No input parameters can be None or empty')
    # raise exception if items of show_columns are not in group_columns
    if not all([(item in group_columns) for item in show_columns]):
       raise Exception('The items of "show_columns" list must be in "group_columns" list')
    # raise exception if the aggregation method is not supported
    if not aggregation in ['count']:
        raise Exception(f'[{aggregation}] method is not supported')
        
    # create group column name to make the aggregation column unique
    group_column_name = aggregation + "_" + "_".join(group_columns)
    # create a empty list
    result = []
    # invoke the aggregation_count method if the aggregation method is "count"
    if aggregation == "count":
        result = aggregation_count(data, group_column_name, group_columns)
        # add the new column name to show_columns to create new data_set if show_columns is not "None"
        if show_columns:
            show_columns.append(group_column_name)
            # send show_columns and data_set to  select_columns function
            return select_columns(result, show_columns)
        else:
            # add the new column name to the columns of the original data set. Because,
            # some unique keys is added to data_set after aggregation process.
            # We should remove these fields from the data_set
            # get columns in the original data set
            data_columns = get_columns(data)
            # append the group column name
            data_columns.append(group_column_name)
            # remove extra fields and create new data set with count
            return select_columns(result, data_columns)


# "count" aggregation method
def aggregation_count(data, group_column_name, group_columns):
    """
    The data filtered by the values inside group_columns to count the filtered rows.
    The result contains some extra fields. These fields can be removed if they will be not used

    Parameters
    ----------
    data : list
        consists of the dictionary items.
        eg : [{"Name":"test", "LastName":"test"} , {"Name":"test", "LastName":"test1"}]

    group_column_name : str
         a unique group column name. eg: "count_Name"

    group_columns : list
        data set is filtered by the values inside group_columns to count. eg: ["Name"]

    Returns
    -------
    list
        the data set with count by group_columns. eg: [{"Name":"test", "count_Name":2, (test,):2}]

    Raises
    ------
    Exception
        If group_column_name is not unique then raise Exception
    """

    if group_column_name in get_columns(data):
        raise Exception(f"{group_column_name} must be unique")

    # create an empty list
    data_group_by_list = []

    for item in data:
        # create tuple key with the values inside data if the key is existing in group_columns
        # this key will be used to find and update the count
        group_by_dict_key = tuple([item[key] for key in item if key in group_columns])
        # filter the data and create a list by group_by_dict_key
        data_group_by_list_filtered = list(filter(lambda data: group_by_dict_key in data, data_group_by_list))
        # if the filtered data was not created before, add new field to dictionary item to keep the count of the row
        if len(data_group_by_list_filtered) == 0:
            group_columns_dict = item.copy()
            group_columns_dict[group_column_name] = 1
            group_columns_dict[group_by_dict_key] = 1
            data_group_by_list.append(group_columns_dict)
        else:
            # the filtered data was created before then just update the count
            for item_filtered in data_group_by_list_filtered:
                item_filtered[group_column_name] = item_filtered[group_column_name] + 1
                item_filtered[group_by_dict_key] = item_filtered[group_by_dict_key] + 1
    # return the new data set with count
    return data_group_by_list


# create data set to use for some statistical methods
def create_data_set(data, key_column, data_set_column):
    """
    Creates a data set to use for some statistical methods by key_column and data_set_column


    Parameters
    ----------
    data : list
        consists of the dictionary items.
        eg : [{"Name":"test", "Year":2000, "Score":1} , {"Name":"test", "Year":2001, "Score":2}]

    key_column : str
         used to find data set value and this value will be key of new data set.
         eg: "Name"

    data_set_column : str
        used to find data set value and this value will be value of new data set
        eg: "Score"

    Returns
    -------
    list
        created new data set by using original data.
        eg: [{"Name":[1,2]}]
    """
    # create an empty list
    result = []
    # The value of dictionary item in data will be key of the new data set
    for item in data:
        # Use key_column to find this value
        result_item_key = item[key_column]
        # The value of the key will be found by using data_set_column
        result_item_data_set_value = item[data_set_column]
        # filter data by result_item_key
        result_filtered = list(filter(lambda data: result_item_key in data, result))
        # if the result has been never populated
        if len(result_filtered) == 0:
            if len(result) == 0:
                result = [{result_item_key: [result_item_data_set_value]}]
            else:
                result.append({result_item_key: [result_item_data_set_value]})
        else:  # if the result has been already populated, just update the data set
            for result_item in result_filtered:
                result_item_values = result_item[result_item_key]
                result_item_values.append(result_item_data_set_value)

    return result


if __name__ == "__main__":
# =============================================================================
     data_set = read_csv(
         "/home/fsusam/Development/workspace/python/standard-deviation/src/examples/data/athlete_events.csv",
         delimiter=';',
         clean_chars_header=['"'])
     print()
     print(f"Sample Row : {sample_rows(data_set, 1)}")
# 
#     data_set = select_columns(data_set, ['NOC', 'Year', 'Medal'])
#     print()
#     print(f"Sample Row selected columns : {sample_rows(data_set, 1)}")
# 
#     print()
#     columns = get_columns(data_set)
#     print(f"Columns : {columns}")
# 
#     print()
     data_set = filter_by(data_set, {"NOC": ['CHN', 'GER'], "Medal": ['Silver', 'Bronze', 'Gold']})
     print(f"Sample row filtered data :{sample_rows(data_set, 1)}")
# 
#     print()
#     data_set = group_by(data_set, group_columns=["NOC", "Year"], show_columns=["NOC", "Year"], aggregation="count")
#     print(f"Sample row group_by data :{sample_rows(data_set, 1)}")
# 
#     print()
#     data_set_plot = create_data_set(data_set, "NOC", "count_NOC_Year")
#     print(f"Sample row data_set_plot :{data_set_plot}")
# 
# =============================================================================
       # data_set = read_csv("/home/fsusam/Development/workspace/python/standard-deviation/src/unit-tests/test_data.csv", clean_chars_header=['"'])
       
       # data_set = filter_by(data_set, filter_values=[{'Name':['User2']}])