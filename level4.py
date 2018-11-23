from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=72198'


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last+"@gmail.com"

    def fullname(self):
        return self.first +' '+self.last

emp_1 = Employee('Peter', 'Smith', 50000)

print(emp_1.fullname())
