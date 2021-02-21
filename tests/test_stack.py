from collections import deque

from second_lab.stack import Stack


def test_stack(mocker):
    mocker.patch('second_lab.stack.Stack.ask_data', return_value=deque([1, 2, 3]))

    assert Stack().result == 4