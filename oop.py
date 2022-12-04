class Employee:

    def __init__(self, first, last, pay):
        # Every class needs their 'self' statement at the beginning for the initiation. The term "Self" is not mandatory, it can be any name, but this is the most used one.
        # We tell python that the class shall be initiated. 
        # HOWEVER: When we initialize a new object with this class (e.g. row 16, 17), the "self"-argument has not to be passed to the class, only the defined attributes.
        # 
        # Attributes are properties of the class, that are created at the initialization. Here, there are following attributes:  
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # As you can see, when creating a new employee, we have to pass all attributes, otherwise it won't work.


    def fullname(self):
        # Besides attributes, there are FUNCTIONS / METHODES that can be created within a class. They serve different purposes.
        # Here we want to print the full name of an employee. Again, as with the class initialization, the "self"-statement IS MANDATORY
        # All attributes associated to the class are already known, and there should not be defined again in the function header.
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Gerald', 'Fruhmann', 42600)
emp2 = Employee('Lena', 'Wicha', 93600)


# -------------------------- KEY TAKE AWAY -------------------------- #
# So no it's getting serious. As you can see, Lumos is created. We pass all necessary arguments. 
# Furthermore, we want to print the last name of Lumos. 

# What really happens when we do that, we can see the line below. When an employee is initiated and we call a function, we certainly do the following:
# Call the Class Employee, use the function fullname and pass this function the "self"-object, in this case: Lumos (or emp3)
emp3 = Employee('Lumos', 'The Greatest', 1000000)
print(emp3.fullname())
print(Employee.fullname(emp3))