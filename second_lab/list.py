import datetime
from typing import Optional, NoReturn, Union


class Person:
    def __init__(self, tab_number: int, dep_number: int, surname: str, wage: int, date: datetime.date,
                 taxes: int, add_percent: int, days_worked: int, days_in_month: int, plus: int, minus: int):
        self.tab_number = tab_number
        self.dep_number = dep_number
        self.surname = surname
        self.wage = wage
        self.date = date
        self.taxes = taxes
        self.add_percent = add_percent
        self.days_worked = days_worked
        self.days_in_month = days_in_month
        self.plus = plus
        self.minus = minus

    def __str__(self):
        return f'Person({self.surname})'

    def __repr__(self):
        return f'Person({self.surname})'


class Solution:
    def __init__(self):
        self.person_list = list()

    def add_persons(self) -> NoReturn:
        self.person_list.append(Person(1, 1, 'Ivanov', 1000, datetime.date(2021, 8, 1), 13, 15, 20, 30, 1000, 100))
        self.person_list.append(Person(432, 5445, 'Petrov', 2000, datetime.date(2020, 1, 5), 13, 15, 21, 31, 2000, 200))
        self.person_list.append(Person(42, 1245, 'Sidorov', 1500, datetime.date(2020, 5, 1), 13, 15, 21, 31, 1400, 1))

    def search_person(self, search_by: str, attribute: str) -> Optional[Person]:
        if search_by == 'date':
            attribute = datetime.date(*map(int, attribute.split('-')))
        elif search_by == 'department number':
            attribute = int(attribute)
        for person in self.person_list:
            if person.__getattribute__(search_by) == attribute:
                return person

    def sort_person(self, sort_attr: str):
        return sorted(self.person_list, key=lambda person: person.__getattribute__(sort_attr), reverse=True)


def menu(obj: Solution) -> Union[list, Person]:
    function = input('input what you want to do:\nsort\nsearch ')
    if function == 'sort':
        attribute = input('input sort attribute:\ndate\ndepartment number\nsurname ')
        return obj.sort_person(attribute)
    elif function == 'search':
        attribute = input('input searching attribute:\ndate\ndepartment number\nsurname ')
        value = input('attribute value: ')
        return obj.search_person(attribute, value)


if __name__ == '__main__':
    s = Solution()
    s.add_persons()
    while True:
        print(menu(s))