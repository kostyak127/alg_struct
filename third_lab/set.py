class Solution:
    def __init__(self):
        self.string = self.ask_data()
        self.letters_set = set()
        self.russian_letters = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    @staticmethod
    def ask_data() -> str:
        return input('input string: ')

    def get_letters(self) -> list:
        for letter in self.string:
            if letter in self.russian_letters:
                self.letters_set.add(letter)
        return sorted(list(self.letters_set))


if __name__ == '__main__':
    s = Solution()
    print(*s.get_letters())
