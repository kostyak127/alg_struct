from array import array


class FirstLabArray:
    def __init__(self):
        self.N = int(input('input array length '))
        self.new_array = self.get_array_from_str(input('input array like 1,2,3,5,6,7... '))
        self.T = int(input('input T '))

        print(self.result)

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


FirstLabArray()
