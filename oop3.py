class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    # Regular Methods in a class, take automatically the instance as the first argument. By convention, that is called "self"
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #Using @classmethod changes the functionality the following: While above using the INSTANCE AS FIRST ARGUMENT, this command gives us the power to use CLASS AS FIRST ARGUMENT.
    # cls is the convention here
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        # Well well well... so far so good. Now we have created first, last, pay variables. HOWEVER, WE HAVE TO TEACH THIS METHODE ALSO, THAT IT HAS TO CREATE A NEW INSTANCE OF THIS CLASS.
        # THEREFORE WE GIVE THEM THE "CLS()" 

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False()
        return True
    # People tend to use classmethods, but the functionality is only a static-method. You can tell it by not accessing any class-variables at all (like here). So no "first", "last", "pay", etc.


emp1 = Employee('Gerald', 'Fruhmann', 42600)
emp2 = Employee('Lena', 'Wicha', 93600)

# When we print it out now, every raise_amout is 1.04, since we defined it in the class
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

# But now we can change it for the whole class!!!! Therefore all instances change! :-) 
Employee.set_raise_amount(1.05)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)


# ------------------------------- Use Case ------------------------------- #
# Hey, I want to create a new employee, by passing a string to the class. Is this possible?
# The information is separated by Hyphens
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

# It's not so clean, to pass the singe 
# strings to the class, therefore we create a new Constructor, that allows us to create a new instance from string directly.
# Therefore we create a new classmothod
# We split it like always in python and the ship the result into the Employee-class. 
# Et voila, we have a new instance of Employee.
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)


# ------------------------------- KEY TAKE AWAY ------------------------------- #
# - Regular Methods: Automatically pass the "self"-object 
# - Class Methods: Automatically pass the "cls"-object --> They can also be used as alternative constructors!
# - Static Methods: don't pass anything automatically, so just like regular functions. we put it in the class, since they may have some logical connection with the class

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))