# Program Name: test_statistical_data_analysis_tool
# Purpose: to test the statistical methods

import sys

sys.path.append('./../')

from pytest import raises, fixture
import file_utils as futl


# create data set which will be used during module test
@fixture(scope='module')
def data_set():
    return [
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2010', 'Score': '5'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '6'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '4'},
        {'Name': "User2", 'LastName': 'User2 Lastname', 'Year': '2011', 'Score': '1'}
    ]


def test_read_csv():
    assert futl.read_csv("test_data.csv") == [
        {'"Name"': "User1", '"LastName"': 'User1 Lastname', '"Year"': '2010', '"Score"': '5'},
        {'"Name"': "User1", '"LastName"': 'User1 Lastname', '"Year"': '2012', '"Score"': '6'},
        {'"Name"': "User1", '"LastName"': 'User1 Lastname', '"Year"': '2012', '"Score"': '4'},
        {'"Name"': "User2", '"LastName"': 'User2 Lastname', '"Year"': '2011', '"Score"': '1'}
    ]

    assert futl.read_csv("test_data.csv", clean_chars_header=['"']) == [
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2010', 'Score': '5'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '6'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '4'},
        {'Name': "User2", 'LastName': 'User2 Lastname', 'Year': '2011', 'Score': '1'}
    ]

    assert futl.read_csv("test_data_no_header.csv", header=False, clean_chars_header=['"']) == [
        {'col_1': "User1", 'col_2': 'User1 Lastname', 'col_3': '2010', 'col_4': '5'},
        {'col_1': "User1", 'col_2': 'User1 Lastname', 'col_3': '2012', 'col_4': '6'},
        {'col_1': "User1", 'col_2': 'User1 Lastname', 'col_3': '2012', 'col_4': '4'},
        {'col_1': "User2", 'col_2': 'User2 Lastname', 'col_3': '2011', 'col_4': '1'}
    ]

    with raises(FileNotFoundError):
        assert futl.read_csv("no_data.csv")


def test_sample_rows(data_set):
    assert futl.sample_rows(data_set) == [{'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2010', 'Score': '5'}]

    assert futl.sample_rows(data_set, count=2) == [
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2010', 'Score': '5'},
        {'Name': "User1", 'LastName': 'User1 Lastname', 'Year': '2012', 'Score': '6'}
    ]


def test_select_columns(data_set):
    assert futl.select_columns(data_set, ['Name', 'Score']) == [
        {'Name': "User1", 'Score': '5'},
        {'Name': "User1", 'Score': '6'},
        {'Name': "User1", 'Score': '4'},
        {'Name': "User2", 'Score': '1'}
    ]


def test_get_columns(data_set):
    assert futl.get_columns(data_set) == ["Name", "LastName", "Year", "Score"]


def test_filter_by(data_set):
    assert futl.filter_by(data_set, filter_values={'Name': ['User2']}) == [
        {'Name': "User2", 'LastName': 'User2 Lastname', 'Year': '2011', 'Score': '1'}
    ]


def test_group_by(data_set):
    assert futl.group_by(data_set, group_columns=['Name', 'Year'], show_columns=["Name", "Year"],
                         aggregation="count") == [
               {'Name': "User1", 'Year': '2010', 'count_Name_Year': 1},
               {'Name': "User1", 'Year': '2012', 'count_Name_Year': 2},
               {'Name': "User2", 'Year': '2011', 'count_Name_Year': 1}
           ]

    with raises(Exception) as e:
        assert futl.group_by(data_set, group_columns=[], show_columns=None, aggregation="count")
    assert str(e.value) == 'No input parameters can be None or empty'

    with raises(Exception) as e:
        assert futl.group_by(data_set, group_columns=['Name', 'Year'], show_columns=["Name", "Year", "Score"],
                             aggregation="count")
    assert str(e.value) == 'The items of "show_columns" list must be in "group_columns" list'

    with raises(Exception) as e:
        assert futl.group_by(data_set, group_columns=['Name', 'Year'], show_columns=["Name", "Year"], aggregation="sum")
    assert str(e.value) == '[sum] method is not supported'


def test_create_data_series(data_set):
    assert futl.create_data_series(data_set, 'Name', 'Score') == [{'User1': ['5', '6', '4']}, {'User2': ['1']}]
