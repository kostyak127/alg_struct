from array import array


class FirstLabArray:
    def __init__(self):
        self.N, self.new_array, self.T = self.ask_data()

        print(self.result)

    def ask_data(self) -> tuple:
        N = int(input('input array length '))
        new_array = self.get_array_from_str(input('input array like 1,2,3,5,6,7... '))
        T = int(input('input T '))
        return N, new_array, T

    @staticmethod  # Need to correct array format after input
    def get_array_from_str(string_array: str) -> array:
        return array('i', [int(elem) for elem in string_array.split(',')])

    @property  # returns program result
    def result(self) -> int:
        result = 1
        is_found = False
        for elem in self.new_array:
            if elem > self.T and not is_found:
                result = result * elem
                is_found = True
            elif is_found:
                result = result * elem

        return result if is_found else 0


if __name__ == '__main__':
    FirstLabArray()