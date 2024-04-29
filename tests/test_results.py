import math
import pathlib
import random
import sys


from typing import Tuple


import numpy as np
import numpy.random as nr
import pytest


DATASET = Tuple[float]


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(0, str(proj_folder))


import main


@pytest.fixture
def expected_percent_as_int() -> int:
    '''
    expected probability in percentage
    '''
    return random.randint(10, 90)


@pytest.fixture
def expected(expected_percent_as_int:int) -> float:
    '''
    expected probability in float
    '''
    return expected_percent_as_int * 0.01


@pytest.fixture
def threshold_value() -> float:
    '''
    function under test would return the probability
        of the elements in the dataset below this value
    '''
    return random.randint(10, 90) + random.uniform(0.1, 0.9)


@pytest.fixture
def data_distribution_factor() -> int:
    '''
    factor for the size of the dataset
    '''
    return random.randint(2, 5)


@pytest.fixture
def data(threshold_value:float, data_distribution_factor:int, expected_percent_as_int:int) -> DATASET:
    '''
    generate a dataset
    the number of elements in the dataset below the threshold value would be
    expected_percent_as_int * data_distribution_factor
    '''
    data_below = nr.uniform(0, int(threshold_value), expected_percent_as_int*data_distribution_factor)
    data_above = nr.uniform(int(threshold_value)+1, threshold_value * 2, (100 - expected_percent_as_int)*data_distribution_factor)
    return tuple(np.concatenate((data_below, data_above)).tolist())


@pytest.fixture
def result(data:DATASET, threshold_value:float) -> float:
    '''
    result of the function under test
    '''
    return main.probability_below(data, threshold_value)


def test_probabilty_below_type(result:float):
    assert isinstance(result, float), f"결과값의 변수형 {type(result)} 이 예상과 다름"


def test_probabilty_below_value(data:DATASET, threshold_value:float, expected:float, result:float):
    assert math.isclose(result, expected), (
        f"결과값 {result} 이 예상 {expected} 와 다름\n"
        f"x_data = {data}\n"
        f"threshold_value = {threshold_value}\n"
    )


if "__main__" == __name__:
    pytest.main([__file__])
