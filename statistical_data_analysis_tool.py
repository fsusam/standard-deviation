#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:25:32 2019

@author: fsusam
"""
# module to calculate standard deviation of data set
# sample data set [10,8,10,8,8,4]

import math

# how spread out your data is in your sample.    
def standard_deviation(data_set):
    # Calculating the Standard Deviation    
    ss=round(math.sqrt(variance(data_set, mean(data_set))), 2)
    print(f"standard deviation: {ss:.2f}")    
    return ss


# calculate the average of the data set
def mean(data_set):    
    mean=sum(data_set)/len(data_set)
    print(f"mean: {mean}")    
    return mean


# how far the data in data set is clustered around the mean
def variance(data_set, mean):
    # find the Variance    
    variance=sum([abs((x-mean)**2) for x in data_set]) / (len(data_set)-1)
    print(f"variance: {variance:.2f}")    
    return variance