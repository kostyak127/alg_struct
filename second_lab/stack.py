from collections import deque
from typing import NoReturn


class Stack:
    def __init__(self):
        self.new_stack = deque()
        self.ask_data()  # input data
        print(self.result)

        self.result_stack = deque()
        self.result_stack.append(self.result)  # add res to stack

    @property
    def result(self):
        result = 0
        while self.new_stack:
            elem = self.new_stack.pop()
            result += elem if elem % 2 else 0
        return result

    def ask_data(self) -> NoReturn:
        stack_length = int(input('input stack length '))

        for _ in range(stack_length):
            self.new_stack.append(int(input('input element to stack ')))


if __name__ == '__main__':
    Stack()
