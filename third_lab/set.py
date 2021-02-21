from typing import NoReturn


class Solution:
    def __init__(self):
        self.string = self.ask_data()
        self.letters_set = set()
        self.russian_letters = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

    @staticmethod
    def ask_data() -> str:
        return input('input string: ')

    def print_letters(self) -> NoReturn:
        for letter in self.string:
            if letter in self.russian_letters:
                self.letters_set.add(letter)

        sorted_letters = sorted(list(self.letters_set))
        for letter in sorted_letters:
            print(letter)


if __name__ == '__main__':
    s = Solution()
    s.print_letters()
