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
    """
    Calculate avarage of data set

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    float
           mean
    """
    # verify data length
    verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='mean')

    # Calculate mean
    return sum(data_set) / len(data_set)


# how far a set of (random) numbers are spread out from their average value
def variance(data_set):
    """
    Calculate how far a set of (random) numbers are spread out from their average value

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    float
           variance
    """
    # verify data length
    verify_data_set_length(expected_length_at_least=2, data_set=data_set, func_name='variance')

    # call mean function to find mean of data set
    average = mean(data_set)
    # find the Variance
    return sum([abs((x - average) ** 2) for x in data_set]) / (len(data_set) - 1)


# middle number in a data set
def median(data_set):
    """
    find the middle number in a data set

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    float
           median
    """
    # verify data length
    verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='median')

    # sort the data set
    data_set.sort()

    return get_item_middle_data_set(data_set)


# calculate correlation
# measure of the linear relationship between two quantitative variables    
def correlation_pearson(data_setx, data_sety):
    """
    Calculate measure of the linear relationship between two quantitative variables

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    float
           pearsonr
    """
    # verify data length
    verify_data_set_length(expected_length_at_least=2, data_set=data_setx, func_name='correlation_pearson')

    # verify data length
    verify_data_set_length(expected_length_at_least=2, data_set=data_sety, func_name='correlation_pearson')

    # data set should have the same length
    if len(data_setx) != len(data_sety):
        raise ValueError("data_setx and data_sety must have the same length.")

    # one of data set length
    n = len(data_setx)
    # calculate mean of data_setx
    mean_x = mean(data_setx)
    # calculate mean of data_sety
    mean_y = mean(data_sety)
    # merge data sets and convert to tuple
    tuple_xy = tuple(zip(data_setx, data_sety))
    # subtract each item of data_setx from itself own mean  and subtract each item of data_sety from itself own mean
    # multiply them each other and sum
    n_sum_tuple = sum([(x - mean_x) * (y - mean_y) for x, y in tuple_xy])
    # calculate std of data_setx
    std_x = standard_deviation(data_setx)
    # calculate std of data_sety
    std_y = standard_deviation(data_sety)
    # calculate pearsonr
    result = n_sum_tuple / ((n - 1) * std_x * std_y)

    return result


# the middle number between the smallest number and the median of the data set.                        
def quartile_first(data_set):
    """
    Find the middle number between the smallest number and the median of the data set

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    float
           quartile (Q1)
    """
    verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='quartile_first')

    # sort the data set
    data_set.sort()

    # find the mid-index
    mid_index = int(len(data_set) / 2)

    return get_item_middle_data_set(data_set[0:mid_index + 1])


# the middle value between the median and the highest value of the data set
def quartile_third(data_set):
    """
    Find the middle value between the median and the highest value of the data set

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    float
           quartile (Q3)
    """
    # verify data length
    verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='quartile_third')

    # sort the data set
    data_set.sort()

    # find the mid-index
    mid_index = int(len(data_set) / 2)

    if len(data_set) % 2:
        # single number in the middle of the data set
        return get_item_middle_data_set(data_set[mid_index:])
    else:
        # two number in the middle of the data set
        return get_item_middle_data_set(data_set[mid_index - 1:])


# min value of data set
def min_data_set(data_set):
    """
    min value of data set

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    Numeric
           min item in the data set
    """
    # verify data length
    verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='min_data_set')

    return min(data_set)


# max value of data set
def max_data_set(data_set):
    """
    max value of data set

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    float
           max item in the data_set
    """
    # verify data length
    verify_data_set_length(expected_length_at_least=1, data_set=data_set, func_name='max_data_set')

    return max(data_set)


# get the item which is the middle of the data set
def get_item_middle_data_set(data_set):
    """
    Find the middle index of the data set and decide the middle of the data set is single or not

    Parameters
    ----------
    data_set : list
           consist of numeric values. eg: [1,2,3,4,5]

    Returns
    -------
    float
           item which is the middle of the data set
    """
    # find the mid-index
    mid_index = int(len(data_set) / 2)

    if len(data_set) % 2:
        # single number in the middle of the data set
        return data_set[mid_index]
    else:
        # two number in the middle of the data set
        return (data_set[mid_index - 1] + data_set[mid_index]) / 2


# common data set length check
def verify_data_set_length(expected_length_at_least, data_set, func_name):
    """
    Verify the data set length by specified data set length

    Parameters
    ----------
    data_set : list
           list of values. eg: [1,2,3,4,5]

    expected_length_at_least : int
           the smallest data point. The data set length can not be less then "expected_length_at_least"

    func_name : str
           invoked function name. eg: "variance" or "mean"

    Raise
    -------
    Exception
           Raise Exception if len(data_set)<expected_length_at_least
    """
    if len(data_set) < expected_length_at_least:
        raise Exception(f"{func_name} requires at least {expected_length_at_least} data points")
