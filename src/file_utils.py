# Program Name: file_utils
# Purpose: Read a file and parse by a delimiter, help to create a new data set


def read_csv(path, delimiter=',', header=True, clean_chars_header=[]):
    result = []
    columns = []
    is_columns_created = False
    split_error_count = 0
    sample_split_error = ''
    
    # read the data from the file
    with open(path) as datafile:
        # for each line in the file
        for line in datafile:
            row = line.strip().split(delimiter)          
        
            # skip first if first line of data is header
            if(not is_columns_created):
                if(header):
                    columns = create_col(row,clean_chars=clean_chars_header)                                        
                else:
                    columns = create_col(col_count=len(row),clean_chars=clean_chars_header)
                
                is_columns_created = True
                continue                
                
            if len(row)!=len(columns):
                split_error_count += 1                
                sample_split_error = line
            else:
                row_dict = {}
                for idx,col_value in enumerate(row):
                    row_dict[columns[idx]] = col_value                    
                result.append(row_dict)
    
    if(split_error_count>0):
        print (f"[{split_error_count}] rows could not be splitted. Sample row : [{sample_split_error}] ")
           
    return result


def select_columns(data, cols):
    selected_columns_data_set = []
    
    for row in data:
        selected_columns_data_set.append(build_row_by_columns(row, cols))
    
    return selected_columns_data_set    


def build_row_by_columns(data_item, cols):               
    row_dict = {}
    for select_col in cols:
        row_dict[select_col] = data_item[select_col]
    return row_dict    
    
        
def sample_rows(data,count):
    return data[:count]


def get_columns(data):
    return [item for item in data[0]] 

        
def create_col(header=None, col_count=None, clean_chars=[]):
    col_names = []
    
    if(header):
        for col_name in header:
            col_names.append(create_column_name(col_names, col_name, clean_chars))
    elif(col_count):
        col_names = [f"col_{i+1}" for i in range(col_count)]
    
    return col_names
            

def create_column_name(col_names, value, clean_chars):
    if value:
        for sc in clean_chars:
            value = ''.join(value.split()).replace(sc,'')
        else:
            value = ''.join(value.split())
        
    col_idx = 1
    
    while True:
        if value in col_names:
            value = f"{value}_{col_idx}"
            col_idx += 1 
        else:
            return value    

def filter_by(data,filter_values):
    filtered_list = data
    
    for filter_col in filter_values:
        filtered_list = list(filter(lambda data: data[filter_col] in filter_values[filter_col], filtered_list))
        
    return filtered_list

def group_by(data, group_columns, show_columns, aggregation):
    if not aggregation in ['count']:
        print(f'[{aggregation}] is not supported')
        return data
    
    group_column_name = aggregation+"_"+"_".join(group_columns)
    
    result = []
    
    if aggregation=="count":
        result = aggregation_count(data, group_column_name, group_columns, show_columns)
    
    show_columns.append(group_column_name)
                          
    return select_columns(result, show_columns)    

def aggregation_count(data, group_column_name, group_columns, show_columns):
    group_columns_dict = {}
    data_group_by_list = []
    
    for item in data:
        # dictionary item 
        group_by_dict_key = tuple([item[key] for key in item if key in group_columns])
        data_group_by_list_filtered = list(filter(lambda data: group_by_dict_key in data, data_group_by_list))
        
        if len(data_group_by_list_filtered)==0:                
            group_columns_dict = build_row_by_columns(item, show_columns)
            group_columns_dict[group_column_name] = 1
            group_columns_dict[group_by_dict_key] = 1
            data_group_by_list.append(group_columns_dict)
        else:    
            for item in data_group_by_list_filtered:
                item[group_column_name] = item[group_column_name] + 1
                item[group_by_dict_key] = item[group_by_dict_key] + 1
     
    return data_group_by_list           
                    
 
def create_data_set(data, key_column, data_set_column ):
    result = []
    
    for item in data:
        result_item_key = item[key_column]
        result_item_data_set_value = item[data_set_column] 
        
        result_filtered = list(filter(lambda data: result_item_key in data, result))
        
        if len(result_filtered)==0:
            if(len(result)==0):
                result = [{ result_item_key: [ result_item_data_set_value ] }]
            else:
                result.append({ result_item_key: [ result_item_data_set_value ] })
        else:
            for result_item in result_filtered:
                result_item_values = result_item[result_item_key]
                result_item_values.append(result_item_data_set_value)
        
                
    return result    
       
if __name__ == "__main__" :
    data_set = read_csv("/home/fsusam/Development/workspace/python/standard-deviation/src/examples/data/athlete_events.csv",clean_chars_header=['"'])
    print()
    print(f"Sample Row : {sample_rows(data_set,1)}" )
    
    data_set = select_columns(data_set, ['NOC', 'Year', 'Medal'] )
    print()
    print(f"Sample Row selected columns : {sample_rows(data_set,1)}" )
    
    print()
    columns = get_columns(data_set)
    print(f"Columns : {columns}")
    
    print()
    data_set = filter_by(data_set, {"NOC":['"CHN"','"GER"'] , "Medal":['"Silver"','"Bronze"','"Gold"']} )
    print(f"Sample row filtered data :{sample_rows(data_set,1)}")
    
    print()
    data_set = group_by(data_set, group_columns=["NOC", "Year"] , show_columns=["NOC", "Year"], aggregation="count")
    print(f"Sample row group_by data :{sample_rows(data_set,1)}")
    
    print()
    data_set_plot = create_data_set(data_set, "NOC", "count_NOC_Year")
    print(f"Sample row data_set_plot :{data_set_plot}")
 