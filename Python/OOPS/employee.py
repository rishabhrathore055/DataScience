class Employee :
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self,id,fname,lname,pay):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@gmail.com'

        Employee.num_of_employees += 1
    def fullname(self):  
        return '{} {}'.format(self.fname,self.lname)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    @classmethod
    def from_str(cls,emp_str):
        id,fname,lname,pay = emp_str.split('-')
        return cls(id,fname,lname,pay)



emp_1 = Employee(2,'mohan','sexena',37000)
emp_2 = Employee(1,'ram','singh',45000)

# print(emp_1.pay) #for knowing the pay of emp_1
# print(emp_1.pay) 
# print(emp_1.__dict__)  
# print(Employee.__dict__) 

# employee.raise_amount = 1.08 #for raise the amount of all the employee presnt in the db
# emp_1.set_raise_amt = 1.05 #for raise the amount of emp_1 only
Employee.set_raise_amt(1.05) 
emp_1.set_raise_amt(1.06)
print(Employee.raise_amt) 
print(emp_1.raise_amt)    
print(emp_2.raise_amt)  

emp_str_1 = '1-John-Doe-70000'
emp_str_2 = '2-Steve-Smith-30000'
emp_str_3 = Employee.from_str('3-Jone-Deck-600')
print(emp_str_3.fname)
print(emp_str_3.email)



 
