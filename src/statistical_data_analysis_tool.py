# provides some statistical data analysis methods
# sample data set [10,8,10,8,8,4]

import math

# a measure of the amount of variation or dispersion of a set of values
def standard_deviation(data_set):
    # Calculate the Standard Deviation
    return math.sqrt(variance(data_set))


# average of the data set
def mean(data_set):
    # Calculate mean
    return sum(data_set)/len(data_set)


# how far a set of (random) numbers are spread out from their average value
def variance(data_set):
    # call mean function to find mean of data set
    average=mean(data_set)
    # find the Variance
    return sum([abs((x-average)**2) for x in data_set]) / (len(data_set)-1)


# middle number in a data set
def median(data_set):
    # sort the data set
    data_set.sort()
    
    return get_item_middle_data_set(data_set)

# calculate correlation
# measure of the linear relationship between two quantitative variables    
def correlation_pearson(data_setx, data_sety):
    
    if len(data_setx)!=len(data_sety) :
        print("Expected all data set length should be same")
        return None
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
                        
def quartile_first(data_set):
    # sort the data set
    data_set.sort()
    
    # find the mid-index
    mid_index = int(len(data_set)/2)
    
    return get_item_middle_data_set(data_set[0:mid_index])


def quartile_third(data_set):
    # sort the data set
    data_set.sort()
    
    # find the mid-index
    mid_index = int(len(data_set)/2)
    
    if len(data_set) % 2:
        return get_item_middle_data_set(data_set[mid_index+1:])
    else:        
        return get_item_middle_data_set(data_set[mid_index:])
    
# min value of data set
def min_data_set(data_set):
    return min(data_set)

# max value of data set
def max_data_set(data_set):
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

    
