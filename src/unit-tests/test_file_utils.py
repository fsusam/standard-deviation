# Program Name: test_file_utils
# Purpose: to test the functions of file_utils

import sys

sys.path.append('./../')

from pytest import raises, fixture
import file_utils as futl


# create data set which will be used during test module
@fixture(scope='module')
def data_set():
    return [
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2010', 'Score': '5'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '6'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '4'},
        {'Name': "User2", 'LastName': 'User2 Lastname', 'Year': '2011', 'Score': '1'}
    ]


# test read_csv function
def test_read_csv():
    # test with a file with header
    # delimiter "," , header=True, clean_chars_header=[]
    # expected all lines in test_data.csv should be in a dictionary list
    assert futl.read_csv("test_data.csv") == [
        {'"Name"': "User1", '"LastName"': 'User1 Lastname', '"Year"': '2010', '"Score"': '5'},
        {'"Name"': "User1", '"LastName"': 'User1 Lastname', '"Year"': '2012', '"Score"': '6'},
        {'"Name"': "User1", '"LastName"': 'User1 Lastname', '"Year"': '2012', '"Score"': '4'},
        {'"Name"': "User2", '"LastName"': 'User2 Lastname', '"Year"': '2011', '"Score"': '1'}
    ]
    # test with clean_chars_header arguments
    # delimiter "," , header=True
    # expected all '"' char in column names in the header should be removed
    assert futl.read_csv("test_data.csv", clean_chars_header=['"']) == [
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2010', 'Score': '5'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '6'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '4'},
        {'Name': "User2", 'LastName': 'User2 Lastname', 'Year': '2011', 'Score': '1'}
    ]
    # test with no header file
    # delimiter ","
    # expected the data set should be created with unique column names
    assert futl.read_csv("test_data_no_header.csv", header=False, clean_chars_header=['"']) == [
        {'col_1': "User1", 'col_2': 'User1 Lastname', 'col_3': '2010', 'col_4': '5'},
        {'col_1': "User1", 'col_2': 'User1 Lastname', 'col_3': '2012', 'col_4': '6'},
        {'col_1': "User1", 'col_2': 'User1 Lastname', 'col_3': '2012', 'col_4': '4'},
        {'col_1': "User2", 'col_2': 'User2 Lastname', 'col_3': '2011', 'col_4': '1'}
    ]
    # expected throw FileNotFoundError exception when the file is not found
    with raises(FileNotFoundError):
        assert futl.read_csv("no_data.csv")


# test sample_rows function
def test_sample_rows(data_set):
    # expected return one line in the data_set
    # count default is 1
    assert futl.sample_rows(data_set) == [{'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2010', 'Score': '5'}]
    # expected return 2 lines in the data set because specified count=2
    assert futl.sample_rows(data_set, count=2) == [
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2010', 'Score': '5'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '6'}
    ]


# test select_columns function
def test_select_columns(data_set):
    # expected the data set should consist of 'Name' and 'Score' columns
    assert futl.select_columns(data_set, ['Name', 'Score']) == [
        {'Name': "User1", 'Score': '5'},
        {'Name': "User1", 'Score': '6'},
        {'Name': "User1", 'Score': '4'},
        {'Name': "User2", 'Score': '1'}
    ]


# test get_columns function
def test_get_columns(data_set):
    # expected return all columns in the data set as a list
    assert futl.get_columns(data_set) == ["Name", "LastName", "Year", "Score"]


# test filter_by function
def test_filter_by(data_set):
    # expected return only "User2" line
    assert futl.filter_by(data_set, filter_values={'Name': ['User2']}) == [
        {'Name': "User2", 'LastName': 'User2 Lastname', 'Year': '2011', 'Score': '1'}
    ]


# test group_by function
def test_group_by(data_set):
    # expected should be grouped by 'Name' and 'Year'
    # expected should sum rows because "count" aggregation method has been specified
    # expected "count_Name_Year" column name should be created by function
    assert futl.group_by(data_set, group_columns=['Name', 'Year'], show_columns=["Name", "Year"],
                         aggregation="count") == [
               {'Name': "User1", 'Year': '2010', 'count_Name_Year': 1},
               {'Name': "User1", 'Year': '2012', 'count_Name_Year': 2},
               {'Name': "User2", 'Year': '2011', 'count_Name_Year': 1}
           ]
    # expected throw exception if the arguments are None or empty expect show_columns
    with raises(Exception) as e:
        assert futl.group_by(data_set, group_columns=[], show_columns=None, aggregation="count")
    assert str(e.value) == 'No input parameters can be None or empty expect show_columns'
    # expected throw exception if the columns in show_columns not in group_columns
    with raises(Exception) as e:
        assert futl.group_by(data_set, group_columns=['Name', 'Year'], show_columns=["Name", "Year", "Score"],
                             aggregation="count")
    assert str(e.value) == 'The items of "show_columns" list must be in "group_columns" list'
    # expected throw exception if aggregation method is not supported
    with raises(Exception) as e:
        assert futl.group_by(data_set, group_columns=['Name', 'Year'], show_columns=["Name", "Year"], aggregation="sum")
    assert str(e.value) == '[sum] method is not supported'


# test create_data_series function
def test_create_data_series(data_set):
    # expected key_column should be "Name" in dictionary and data_series_column should be consist of "Score" values
    assert futl.create_data_series(data_set, key_column='Name', data_series_column='Score') == [
        {'User1': ['5', '6', '4']}, {'User2': ['1']}]
