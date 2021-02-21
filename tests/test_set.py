import pytest

from third_lab.set import Solution


def test_set(mocker):
    mocker.patch('third_lab.set.Solution.ask_data', return_value='Привет, я Костя')
    s = Solution()
    assert s.get_letters() == ["е", "и", "о", "я"]