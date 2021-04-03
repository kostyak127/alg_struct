from collections import deque


class Stack:
    def __init__(self):
        self.new_stack = self.ask_data()  # input data and write it to stack
        self.result = self.count_result()

        # self.result_stack = deque()
        self.new_stack.append(self.result)  # add res to stack

    def count_result(self):
        result = 0
        while self.new_stack:
            elem = self.new_stack.pop()
            result += elem if elem % 2 else 0

        return result

    @staticmethod
    def ask_data() -> deque:
        new_stack = deque()
        stack_length = int(input('input stack length '))

        for _ in range(stack_length):
            new_stack.append(int(input('input element to stack ')))

        return new_stack


if __name__ == '__main__':
    Stack()
