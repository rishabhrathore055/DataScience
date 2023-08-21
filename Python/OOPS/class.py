# Python Object_oreinted Programming
class Employee:
    def __init__(self,first,last, branch,adyear,enollno):
        self.first = first
        self.last = last
        self.age = branch
        self.adyear = adyear
        self.enollno = enollno
        self.email = first + '.' + last + branch + adyear+ '@indoreinstitute.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
 
emp_1 = Employee('ram','singh','it','2020','45')
emp_2 = Employee('ansh','prajapati','it','2021','20')
# print(emp_1.email)
# print(emp_1.fullname())
print(emp_1.fullname()) 
print(Employee.fullname(emp_2))