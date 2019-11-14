#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:25:32 2019

@author: fsusam
"""
# provides some statistical data analysis methods
# sample data set [10,8,10,8,8,4]

import math

# a measure of the amount of variation or dispersion of a set of values
def standard_deviation(data_set):
    # Calculate the Standard Deviation    
    ss=round(math.sqrt(variance(data_set)), 2)
    print(f"standard deviation: {ss:.2f}")    
    return ss


# average of the data set
def mean(data_set):
    # Calculate mean        
    mean=sum(data_set)/len(data_set)
    print(f"mean: {mean}")    
    return mean


# how far a set of (random) numbers are spread out from their average value
def variance(data_set):
    # call mean function
    average=mean(data_set)
    # find the Variance    
    variance=sum([abs((x-average)**2) for x in data_set]) / (len(data_set)-1)
    print(f"variance: {variance:.2f}")    
    return variance

# middle number in a data set
def median(data_set):
    # sort the list
    data_set.sort()
    
    # find the mid-index
    mid_index = int(len(data_set)/2)
        
    if len(data_set) % 2:
        # single number in the middle of the data set
        return data_set[mid_index]
    else: 
        # two number in the middle of the data set
        return (data_set[mid_index-1] + data_set[mid_index])/2
