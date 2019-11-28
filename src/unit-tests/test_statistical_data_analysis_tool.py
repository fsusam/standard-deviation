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
def simple_data1():
       return [7, 5, 6, 4, 3]

@fixture(scope='module')
def simple_data_single_value():
       return [1]

@fixture(scope='module')
def simple_data_empty():
       return []

def test_min_dataset(simple_data, simple_data_empty):
       # expect error if data set is empty
       with raises(Exception) as e:
              assert sdat.min_data_set(simple_data_empty)
       assert str(e.value) == "min_data_set requires at least 1 data points"
       
       assert sdat.min_data_set(simple_data) == 1

def test_max_dataset(simple_data, simple_data_empty):
       # expect error if data set is empty
       with raises(Exception) as e:
              assert sdat.max_data_set(simple_data_empty)
       assert str(e.value) == "max_data_set requires at least 1 data points"
       
       assert sdat.max_data_set(simple_data) == 5 
    
def test_mean(simple_data, simple_data_single_value, simple_data_empty):
       # expect error if data set is empty
       with raises(Exception) as e:
              assert sdat.mean(simple_data_empty)
       assert str(e.value) == "mean requires at least 1 data points"
       
       assert sdat.mean(simple_data) == 3
       assert sdat.mean(simple_data_single_value) == 1

def test_median(simple_data, simple_data_single_value, simple_data_empty):
       # expect error if data set is empty
       with raises(Exception) as e:
              assert sdat.median(simple_data_empty)
       assert str(e.value) == "median requires at least 1 data points"
       
       assert sdat.median(simple_data) == 3
       assert sdat.median(simple_data_single_value) == 1

def test_quartile_first(simple_data, simple_data_single_value, simple_data_empty):
       # expect error if data set is empty
       with raises(Exception) as e:
              assert sdat.quartile_first(simple_data_empty)
       assert str(e.value) == "quartile_first requires at least 1 data points"
       
       assert sdat.quartile_first(simple_data) == 2
       assert sdat.quartile_first(simple_data_single_value) == 1

def test_quartile_third(simple_data, simple_data_single_value, simple_data_empty):
       # expect error if data set is empty
       with raises(Exception) as e:
              assert sdat.quartile_third(simple_data_empty)
       assert str(e.value) == "quartile_third requires at least 1 data points"
       
       assert sdat.quartile_third(simple_data) == 4
       assert sdat.quartile_third(simple_data_single_value) == 1  
    
def test_variance(simple_data, simple_data_single_value):
       # expect error if data set length less than 2
       with raises(Exception) as e:
              assert sdat.variance(simple_data_single_value)
       
       assert str(e.value) == "variance requires at least 2 data points"
       assert sdat.variance(simple_data) == 2.5
     
def test_standard_deviation(simple_data, simple_data_single_value):
       # this func invoke variance func
       # expect error if data set length less than 2
       with raises(Exception) as e:
              assert sdat.standard_deviation(simple_data_single_value)
              
       assert str(e.value) == "variance requires at least 2 data points"       
       assert sdat.standard_deviation(simple_data) == approx(1.581138)
    

def test_correlation_pearson(simple_data, simple_data1, simple_data_single_value):
       # expect error if data set length less than 2
       with raises(Exception) as e:
              assert sdat.correlation_pearson(simple_data,simple_data_single_value)
              
       assert str(e.value) == "correlation_pearson requires at least 2 data points"       
       
       # expect error if data set length are not same
       with raises(Exception) as e:
              assert sdat.correlation_pearson(simple_data, [1,2,3])
              
       assert str(e.value) == "data_setx and data_sety must have the same length."
       
       assert sdat.correlation_pearson(simple_data, simple_data1) == -0.9    
  

     