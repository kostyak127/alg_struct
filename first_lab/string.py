class FirstLabString:
    def __init__(self):
        self.word_string = self.ask_data()
        print(self.result)

    @staticmethod
    def ask_data() -> str:
        return input('input string with words')

    @property
    def result(self) -> str:
        biggest_word_length = 0
        biggest_word = ''
        for word in self.word_string.split():
            if len(word) > biggest_word_length:
                biggest_word = word
                biggest_word_length = len(word)
        return biggest_word if biggest_word else 'string with words empty'


if __name__ == '__main__':
    FirstLabString()
