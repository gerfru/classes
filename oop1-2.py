class Employee:
    
    # Welcome to class variables :-)
    num_of_emp = 0 
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Every class needs their 'self' statement at the beginning for the initiation. The term "Self" is not mandatory, it can be any name, but this is the most used one.
        # We tell python that the class shall be initiated. 
        # HOWEVER: When we initialize a new object with this class (e.g. row 16, 17), the "self"-argument has not to be passed to the class, only the defined instance-variables.
        # 
        # Instances-Variables are properties of the class, that are created at the initialization. Here, there are following attributes:  
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # As you can see, when creating a new employee, we have to pass all variables, otherwise it won't work.

        # We want to keep track of the number of employees. Since it does not make sense, that this number is different for every instance, we use "Employee"    
        Employee.num_of_emp += 1

        # Different to that, there are also class-variables, that are the same with every instance. Instance-Variables are depending on the arguments passed to the class.
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
        # -------------------------- So there is a KEY TAKE AWAY -------------------------- #
        # The line above would also work with: self.pay = int(self.pay * Employee.raise_amount)
        # The difference would be, that the usage of "Employee" instead of "self" leads to the fact, that the raise amount would be fore EVERY Instance the same. (as defined in the class variable)
        # Using "self" allows us to change that amount for every instance :-)  

    def fullname(self):
        # Besides attributes, there are FUNCTIONS / METHODES that can be created within a class. They serve different purposes.
        # Here we want to print the full name of an employee. Again, as with the class initialization, the "self"-statement IS MANDATORY
        # All attributes associated to the class are already known, and there should not be defined again in the function header.
        return '{} {}'.format(self.first, self.last)


print(Employee.num_of_emp) #Result: 0
emp1 = Employee('Gerald', 'Fruhmann', 42600)
emp2 = Employee('Lena', 'Wicha', 93600)


# -------------------------- KEY TAKE AWAY -------------------------- #
# So no it's getting serious. As you can see, Lumos is created. We pass all necessary arguments. 
# Furthermore, we want to print the last name of Lumos. 

# What really happens when we do that, we can see the line below. When an employee is initiated and we call a function, we certainly do the following:
# Call the Class Employee, use the function fullname and pass this function the "self"-object, in this case: Lumos (or emp3)
#emp3 = Employee('Lumos', 'The Greatest', 1000000)
#print(emp3.fullname())
#print(Employee.fullname(emp3))

# Lesson 2
# We defined a method "apply_raise" that takes a raise. Within this method, we defined, that the raise shall be 4% (1.04). So it works, but we still want to make cleaner code.
# Therefore, we take the "apply_raise"-factor out ot the method and create a nice class variable.
# Accessing that variable like this :-) 
print(Employee.raise_amount) #Result: 1.04
print(emp1.raise_amount) #Result 1.04
print(emp2.raise_amount) #Result: 1.04

# So the nice thing is really that:
print (emp1.__dict__) # that shows us all the attributes created
# Result: {'first': 'Gerald', 'last': 'Fruhmann', 'pay': 42600, 'email': 'Gerald.Fruhmann@company.com'}
# there is no raise_amount, because it has not created yet.

# When we do that with:
print(Employee.__dict__) # it shows us
#Result: {'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x000001852686A170>, 'apply_raise': <function Employee.apply_raise at 0x000001852686A200>, 'fullname': <function Employee.fullname at 0x000001852686A290>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
# the raise_amount variable is part of the class

# When we do know:
emp1.raise_amount = 1.05
print(emp1.__dict__) # Result: {'first': 'Gerald', 'last': 'Fruhmann', 'pay': 42600, 'email': 'Gerald.Fruhmann@company.com', 'raise_amount': 1.05}
# So it has been created, by passing it to the instance "emp1" of Employee :-) 
# It does that finding in its own namespace, before searching the class.

print(Employee.raise_amount) #Result: 1.04
print(emp1.raise_amount) #Result 1.04
print(emp2.raise_amount) #Result: 1.04

print(Employee.num_of_emp) #Result: 2