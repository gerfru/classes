class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp1 = Employee('Gerald', 'Fruhmann', 42600)
emp2 = Employee('Lena', 'Wicha', 93600)


print(Employee.raise_amt)
emp2.raise_amt = 2
print(emp1.raise_amt)
print(emp2.raise_amt)