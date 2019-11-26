import sys

sys.path.append('./../')

from file_utils import read_csv

lines = read_csv("/home/fsusam/Development/workspace/python/standard-deviation/src/examples/athlete_events.csv", # file path
                 specified_column_list=[0,7,9,-1], # get only specified columns
                 filter_by={7:('"GER"','"CHN"'),-1:('"Silver"','"Bronze"','"Gold"')} # filter by specfied values
                 )
medal_count_by_noc= {}

for id, noc, year, medal in lines:
    # remove '"' character and get only country code
    cleaned_noc = noc[1:-1]    
    # if there is no any key with country code in the dictionary, create a new one  
    if not cleaned_noc in medal_count_by_noc:
        medal_count_by_noc [cleaned_noc] = [{int(year) : 1}]
    else: # if it is found one key inside dictionary get the values of the key
        medal_count_by_year_list = medal_count_by_noc[cleaned_noc]
        for idx, item in enumerate(medal_count_by_year_list): # assign index and item of the list for each iteration
            if int(year) in item: # the item should be dictionary type and check if the key is defined or not
                medal_count_by_year_list[idx] = {int(year) : item[int(year)] + 1} # if it is found one increase the medal count and update the list
                break # exit from for-loop
        else:
            medal_count_by_year_list.append({int(year) : 1}) # if it is not found the key create a new dictionary and append to the list
            
print(f"{medal_count_by_noc}")          
