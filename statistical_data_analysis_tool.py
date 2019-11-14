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