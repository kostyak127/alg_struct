import pytest

from first_lab.string import FirstLabString


def test_result_if_biggest_exists(mocker):
    mocker.patch('first_lab.string.FirstLabString.ask_data', return_value='abc defg hijkl')

    assert FirstLabString().result == 'hijkl'


def test_result_if_biggest_not_exists(mocker):
    mocker.patch('first_lab.string.FirstLabString.ask_data', return_value='')

    assert FirstLabString().result == 'string with words empty'
