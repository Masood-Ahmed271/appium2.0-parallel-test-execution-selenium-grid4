# in pytest file name should be named as test_*.py
# only functions with name test_* will be executed

## Example

'''
import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11
'''

# To run: `pytest -v` it runs all the tests in the current directory
# To run a specific file: `pytest -v test_sample.py`
# To execute the tests containing a string in its name we can use the following syntax − pytest -k <substring> -v example − pytest -k square -v


# Pytest provides two ways to run the subset of the test suite.

#     Select tests to run based on substring matching of test names.
#     Select tests groups to run based on the markers applied.


# Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.

# A function is marked as a fixture by −

# @pytest.fixture

# A test function can use a fixture by mentioning the fixture name as an input parameter.

# Create a file test_div_by_3_6.py and add the below code to it

# import pytest

# @pytest.fixture
# def input_value():
#    input = 39
#    return input

# def test_divisible_by_3(input_value):
#    assert input_value % 3 == 0

# def test_divisible_by_6(input_value):
#    assert input_value % 6 == 0

# Here, we have a fixture function named input_value, which supplies the input to the tests. To access the fixture function, the tests have to mention the fixture name as input parameter.

# Pytest while the test is getting executed, will see the fixture name as input parameter. It then executes the fixture function and the returned value is stored to the input parameter, which can be used by the test.



# we can run tests by using the syntax pytest -n <num>

# pytest -n 3

# -n <num> runs the tests by using multiple workers, here it is 3 workers.

# To get results of the tests in a file we can use the following syntax − pytest -v --junitxml="results.xml"