# Program Name: test_statistical_data_analysis_tool
# Purpose: to test the statistical methods

import sys

sys.path.append('./../')

from  pytest import approx , fixture, raises
import statistical_data_analysis_tool as sdat

# create data set which will be used during module test
@fixture(scope='module')
def simple_data():
       return [1, 2, 3, 4, 5]

@fixture(scope='module')
def simple_data_single_value():
       return [1]

def test_min_dataset(simple_data):
       assert sdat.min_data_set(simple_data) == 1

def test_max_dataset(simple_data):
       assert sdat.max_data_set(simple_data) == 5 
    
def test_mean(simple_data, simple_data_single_value):
       assert sdat.mean(simple_data) == 3
       assert sdat.mean(simple_data_single_value) == 1

def test_median(simple_data, simple_data_single_value):
       assert sdat.median(simple_data) == 3
       assert sdat.median(simple_data_single_value) == 1

def test_quartile_first(simple_data, simple_data_single_value):
       assert sdat.quartile_first(simple_data) == 2
       assert sdat.quartile_first(simple_data_single_value) == 1

def test_quartile_third(simple_data, simple_data_single_value):
       assert sdat.quartile_third(simple_data) == 4
       assert sdat.quartile_third(simple_data_single_value) == 1  
    
def test_variance(simple_data, simple_data_single_value):
       # expect error if data set length less than 2
       with raises(Exception) as e:
              assert sdat.variance(simple_data_single_value)
       
       assert str(e.value) == "variance requires at least two data points"
       assert sdat.variance(simple_data) == 2.5
#     
def test_standard_deviation(simple_data):
       # this func invoke variance func
       # expect error if data set length less than 2
       with raises(Exception) as e:
              assert sdat.variance(simple_data_single_value)
              
       assert str(e.value) == "variance requires at least two data points"       
       assert sdat.standard_deviation(simple_data) == approx(1.581138)
    

    
  

     