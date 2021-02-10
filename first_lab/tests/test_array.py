from random import randint

import pytest
from array import array

from first_lab.array import FirstLabArray


def test_get_array_from_str():
    string_array = '1,2,3,4'

    assert FirstLabArray.get_array_from_str(string_array) == array('i', [1, 2, 3, 4])


def test_result_array_if_bigger_exits(mocker):
    mocker.patch('first_lab.array.FirstLabArray.ask_data', return_value=(4, array('i', [1, 2, 3, 4]), 2))

    assert FirstLabArray().result == 12


def test_result_array_if_bigger_not_exists(mocker):
    mocker.patch('first_lab.array.FirstLabArray.ask_data', return_value=(4, array('i', [1, 2, 3, 4]), 99))
    assert FirstLabArray().result == 0