from Lib import queue


class Solution:
    def __init__(self):
        self.raw_data = self.get_list_from_str(input('input data like 1,2,3,4 '))
        self.odd = queue.PriorityQueue()
        self.even = queue.PriorityQueue()

    @staticmethod  # Need to correct array format after input
    def get_list_from_str(string_array: str) -> list:
        return [int(elem) for elem in string_array.split(',')]

    def pull_queues(self):
        for elem in self.raw_data:
            if elem % 2:
                self.odd._put(elem)
            else:
                self.even._put(elem)
        print(self.odd._get())

if __name__ == '__main__':
    Solution().pull_queues()
