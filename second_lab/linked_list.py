import datetime


class Person:
    def __init__(self, tab_number: int, dep_number: int, surname: str, wage: int, date: datetime.date,
                 taxes: int, add_percent: int, days_worked: int, days_in_month: int, plus: int, minus: int,
                 next=None):
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
        self.next = next

    def __str__(self):
        return f'Person({self.surname})'

    def __repr__(self):
        return f'Person({self.surname})'


class LinkedList:
    def __init__(self):
        self.first_item = None
        self.last_item = None
        self.length = 0

    def add(self, person_data):
        self.length += 1
        if self.first_item is None:
            self.last_item = self.first_item = Person(*person_data, None)
        else:
            self.last_item.next = self.last_item = Person(*person_data, None)

    def find_item(self, attribute, value):
        current_item = self.first_item
        while current_item is not None:
            if current_item.__getattribute__(attribute) == value:
                return current_item
            current_item = current_item.next

    def sort_items(self, attribute):
        current_item = self.first_item
        head = self.first_item
        while current_item.next is not None:
            if current_item.next and current_item.__getattribute__(attribute) > current_item.next.__getattribute__(
                    attribute):
                current_item = current_item.next
            else:
                temp = current_item.next
                current_item.next = temp.next
                if head.__getattribute__(attribute) > temp.__getattribute__(attribute):
                    temp.next = head
                    self.first_item = temp
                    head = temp
                else:
                    inpos = head
                    try:
                        while temp.__getattribute__(attribute) > inpos.next.__getattribute__(attribute):
                            inpos = inpos.next
                    except AttributeError:
                        temp.next = None
                        inpos.next = temp
                        self.show_items()
                        break
                    temp.next = inpos.next
                    inpos.next = temp
        # self.show_items()

    def show_items(self):
        current_item = self.first_item
        while current_item is not None:
            print(current_item)
            current_item = current_item.next


if __name__ == '__main__':
    L = LinkedList()
    L.add((1, 1, 'Ivanov', 1000, datetime.date(2021, 8, 1), 13, 15, 20, 30, 1000, 100))
    L.add((432, 5445, 'Petrov', 2000, datetime.date(2020, 1, 5), 13, 15, 21, 31, 2000, 200))
    L.add((431, 5445, 'Petr', 2000, datetime.date(2020, 1, 5), 13, 15, 21, 31, 2000, 200))
    L.add((42, 1245, 'Sidorov', 1500, datetime.date(2020, 5, 1), 13, 15, 21, 31, 1400, 1))
    L.sort_items('tab_number')
    # L.show_items()
