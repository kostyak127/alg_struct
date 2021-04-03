import queue


# class MyQueue(queue.PriorityQueue):
#     def put(self, elem, **kwargs):
#         self._put(elem)
#
#     def get(self, **kwargs):
#         return self._get()


class Solution:
    def __init__(self):
        self.raw_data = self.get_list_from_str(input('input data like 1,2,3,4 '))
        self.odd = queue.PriorityQueue()
        self.even = queue.PriorityQueue()

    @staticmethod  # Need to correct array format after input
    def get_list_from_str(string_array: str) -> list:
        return [int(elem) for elem in string_array.split(',')]

    def pull_queues_1(self):
        for elem in self.raw_data:
            if elem % 2:
                self.odd.put(elem)
            else:
                self.even.put(elem)
        print(self.odd.get())
        print(self.even.get())

    def pull_queues_2(self):
        for i, elem in enumerate(self.raw_data):
            if (i + 1) % 2:
                self.odd.put(elem)
            else:
                self.even.put(elem)
        print(self.odd.get())
        print(self.even.get())

if __name__ == '__main__':
    Solution().pull_queues_2()
