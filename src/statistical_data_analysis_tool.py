# Program Name: statistical_data_analysis_tool
# Purpose: provide  some statistical data analysis methods


import math


# a measure of the amount of variation or dispersion of a set of values
def standard_deviation(data_set):
       """
       Calculate standard deviation

       Parameters
       ----------
       data_set : list
              consist of numeric values. eg: [1,2,3,4,5]
      
       Returns
       -------
       float
              standard deviation.
       """
       # Calculate the Standard Deviation
       return math.sqrt(variance(data_set))


# average of the data set
def mean(data_set):
       # verify data length
       verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='mean')
    
       # Calculate mean
       return sum(data_set)/len(data_set)


# how far a set of (random) numbers are spread out from their average value
def variance(data_set):
       # verify data length
       verify_data_set_length(expected_length_at_least=2, data_set=data_set, func_name='variance')
       
       # call mean function to find mean of data set
       average=mean(data_set)
       # find the Variance
       return sum([abs((x-average)**2) for x in data_set]) / (len(data_set)-1)


# middle number in a data set
def median(data_set):
       # verify data length
       verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='median')
    
       # sort the data set
       data_set.sort()
    
       return get_item_middle_data_set(data_set)


# calculate correlation
# measure of the linear relationship between two quantitative variables    
def correlation_pearson(data_setx, data_sety):
    
       # verify data length
       verify_data_set_length(expected_length_at_least=2, data_set=data_setx, func_name='correlation_pearson')
       
       # verify data length
       verify_data_set_length(expected_length_at_least=2, data_set=data_sety, func_name='correlation_pearson')
       
       # data set should have the same length
       if len(data_setx)!=len(data_sety) :
              raise ValueError("data_setx and data_sety must have the same length.")
       
       # one of data set length
       n= len(data_setx)
    
       # merge data sets and convert to tuple
       tuple_xy = tuple(zip(data_setx,data_sety))
       # multiply by each other every x and y items which comes from tuple and multiply by length     
       n_sum_tuple = n*sum([x*y for x,y in tuple_xy])
       # sum x and y data set
       sum_x = sum(data_setx)
       sum_y = sum(data_sety)

       # sum pow(x,2) and multiply by n
       n_sum_x_pow2 = n*sum([x**2 for x in data_setx])
       n_sum_y_pow2 = n*sum([y**2 for y in data_sety])
    
       # sum pow(sum(x),2)
       sum_x_pow2 = sum_x**2
       sum_y_pow2 = sum_y**2
    
       # calculate pearson correlation
       result = (n_sum_tuple - (sum_x * sum_y)) / math.sqrt((n_sum_x_pow2 - sum_x_pow2) * (n_sum_y_pow2 - sum_y_pow2))
    
       return result      


# find quartile %25                        
def quartile_first(data_set):
       # verify data length
       verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='quartile_first')
       
       # sort the data set
       data_set.sort()
    
       # find the mid-index
       mid_index = int(len(data_set)/2)
    
       return get_item_middle_data_set(data_set[0:mid_index+1])


# find quartile %75
def quartile_third(data_set):
       # verify data length
       verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='quartile_third')
       
       # sort the data set
       data_set.sort()
    
       # find the mid-index
       mid_index = int(len(data_set)/2)
    
       if len(data_set) % 2:
              # single number in the middle of the data set
              return get_item_middle_data_set(data_set[mid_index:])
       else:
              # two number in the middle of the data set
              return get_item_middle_data_set(data_set[mid_index-1:])
 
       
# min value of data set
def min_data_set(data_set):
       # verify data length
       verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='min_data_set')
       
       return min(data_set)


# max value of data set
def max_data_set(data_set):
       # verify data length
       verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='max_data_set')
    
       return max(data_set)


# find the median and check single number in the middle of the data set or not
def get_item_middle_data_set(data_set):
    # find the mid-index
    mid_index = int(len(data_set)/2)
    
    if len(data_set) % 2:
        # single number in the middle of the data set
        return data_set[mid_index]                
    else: 
        # two number in the middle of the data set
        return (data_set[mid_index-1] + data_set[mid_index])/2


# common data set length check
def verify_data_set_length(expected_length_at_least, data_set, func_name):
       if len(data_set)<expected_length_at_least :
           raise Exception(f"{func_name} requires at least {expected_length_at_least} data points")
