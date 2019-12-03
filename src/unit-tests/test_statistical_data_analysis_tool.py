# Program Name: test_statistical_data_analysis_tool
# Purpose: to test the statistical methods

# to access file_utils and its functions
import sys

sys.path.append('./../')

# test framework
from pytest import approx, fixture, raises
# module that will be tested
import statistical_data_analysis_tool as sdat


# create data set which will be used during test module
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


# test min_dataset function
def test_min_dataset(simple_data, simple_data_empty):
    # expected error if data set is empty
    with raises(Exception) as e:
        assert sdat.min_data_set(simple_data_empty)
    assert str(e.value) == "min_data_set requires at least 1 data points"
    # expected return 1 because it is min value of the data set
    assert sdat.min_data_set(simple_data) == 1


# test max_dataset function
def test_max_dataset(simple_data, simple_data_empty):
    # expected error if data set is empty
    with raises(Exception) as e:
        assert sdat.max_data_set(simple_data_empty)
    assert str(e.value) == "max_data_set requires at least 1 data points"
    # expected return 5 because it is max value of the data set
    assert sdat.max_data_set(simple_data) == 5


# test mean function
def test_mean(simple_data, simple_data_single_value, simple_data_empty):
    # expected error if data set is empty
    with raises(Exception) as e:
        assert sdat.mean(simple_data_empty)
    assert str(e.value) == "mean requires at least 1 data points"
    # expected return average of the data set
    # reference point : https://www.wikihow.com/Find-Mean%2C-Median%2C-and-Mode
    assert sdat.mean(simple_data) == 3
    # expected return the item of list if it has only one item
    assert sdat.mean(simple_data_single_value) == 1


# test median function
def test_median(simple_data, simple_data_single_value, simple_data_empty):
    # expected error if data set is empty
    with raises(Exception) as e:
        assert sdat.median(simple_data_empty)
    assert str(e.value) == "median requires at least 1 data points"
    # expected return median of the data set
    assert sdat.median(simple_data) == 3
    # expected return the item of list if it has only one item
    assert sdat.median(simple_data_single_value) == 1


# test quartile_first function
def test_quartile_first(simple_data, simple_data_single_value, simple_data_empty):
    # expected error if data set is empty
    with raises(Exception) as e:
        assert sdat.quartile_first(simple_data_empty)
    assert str(e.value) == "quartile_first requires at least 1 data points"
    # expected return Q1
    assert sdat.quartile_first(simple_data) == 2
    # expected return the item of list if it has only one item
    assert sdat.quartile_first(simple_data_single_value) == 1


# test quartile_third function
def test_quartile_third(simple_data, simple_data_single_value, simple_data_empty):
    # expected error if data set is empty
    with raises(Exception) as e:
        assert sdat.quartile_third(simple_data_empty)
    assert str(e.value) == "quartile_third requires at least 1 data points"
    # expected return Q3
    assert sdat.quartile_third(simple_data) == 4
    # expected return the item of list if it has only one item
    assert sdat.quartile_third(simple_data_single_value) == 1


# test variance function
def test_variance(simple_data, simple_data_single_value):
    # expected error if data set length less than 2
    with raises(Exception) as e:
        assert sdat.variance(simple_data_single_value)
    assert str(e.value) == "variance requires at least 2 data points"
    # expected return variance
    # reference point : https://www.wikihow.com/Calculate-Variance
    assert sdat.variance(simple_data) == 2.5


# test standard_deviation function
def test_standard_deviation(simple_data, simple_data_single_value):
    # this func invoke variance func
    # expected error if data set length less than 2
    with raises(Exception) as e:
        assert sdat.standard_deviation(simple_data_single_value)
    assert str(e.value) == "variance requires at least 2 data points"
    # expected return standard deviation
    # reference point : https://www.wikihow.com/Calculate-Standard-Deviation
    assert sdat.standard_deviation(simple_data) == approx(1.581138)


# test correlation_pearson function
def test_correlation_pearson(simple_data, simple_data1, simple_data_single_value):
    # expected error if data set length less than 2
    with raises(Exception) as e:
        assert sdat.correlation_pearson(simple_data, simple_data_single_value)
    assert str(e.value) == "correlation_pearson requires at least 2 data points"
    # expected error if data set length are not same
    with raises(Exception) as e:
        assert sdat.correlation_pearson(simple_data, [1, 2, 3])
    assert str(e.value) == "data_setx and data_sety must have the same length."
    # expected return pearson correlation coefficient
    # reference point : https://www.wikihow.com/Calculate-Pearson-Correlation-Coefficient
    assert sdat.correlation_pearson(simple_data, simple_data1) == approx(-0.8999999)
