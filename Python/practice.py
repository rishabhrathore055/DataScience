# print("Hello world!")
# List Slicling
# my_list =[10,20,30,40,50,60,70,80,90,100]
#    0, 1, 2, 3, 4, 5, 6, 7, 8, 
#  -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
# list[start:end]
# print(my_list[-1])
# print(max(my_list))
# print(min(my_list))
# print(my_list[0:-6])
# list[start:end:step]
# print(my_list[1:9:3])
# print(my_list[0:9:2])
# print(my_list[1 :10:2])

# sample_url = 'http://coreyms.com'
# print(sample_url)

# Reverse the url
# print(sample_url[::-1])

# # Get the top level domain
# print(sample_url[-4:])

# # Print the url without the http://
# print sample_url[7:]

# # Print the url without the http:// or the top level domain
# print(sample_url[7:-4])

# List Comprehension
# nums =[2,4,6,8,10,12,15,16,18,20]

# my_list = []
# for n in nums :
#         my_list.append(n)
# print(my_list) 
#        
# my_list = [n for n in nums]
# print(my_list)

# Now I Want To Print Square of the numbers
# my_list = []
# for n in nums:
#         my_list.append(n**2)
# print(my_list)
# my_list = [n**2 for n in nums]
# print(my_list)

# Using a map + lambda
# my_list = list(map(lambda n: n*n, nums))
# print(my_list)
  
# num = [1,2,3,4,5,6,7,8]
# my_list = []
# for n in numbers:
#         if n%2 ==0:
#            my_list.append(n)
# print(my_list)   
# my_list =[]
# for n in num:
#         if n%2 ==1:
#                 my_list.append(n)
# print(my_list)                
# my_list = [n for n in numbers if n%2==0]
# my_list = [ n for n in num if n%2==1]
# print(my_list)

# Using a Filter + lambda

# my_list = list(filter(lambda n: n%2==0, numbers))
# print(my_list)

# I want a (letter, num) pair for each letter in 'Indore' and each number in '0123'
# my_list = []
# for letter in 'indore':
#         for num in range(5):
#                 my_list.append((letter,num))
# print(my_list)

# my_list = [(letter,num) for letter in 'indore' for num in range(5)]
# print(my_list)


# Dictionary Comprehension
# name = ['Puneet','Mohit','Aditya','Ashwin','Mukund','Rishabh']
# skills =['C++','Python','Cloud','WebD','frontend','Data Science']
# print(list(zip(name,skills)))

# my_dict = {}
# for name,skills in zip(name,skills):
#         my_dict[name] = skills
# print(my_dict)

# my_dict = {name : skills for name, skills in zip (name,skills) if name!='Mukund'}
# print(my_dict) 
# Set Comprehension
# nums = [1,1,2,4,3,5,3,4,6,7,8,2,9,9]
# my_set = set()
# for n in nums:
#         my_set.add(n)
# print(my_set)        

# my_set= {n for n in nums}
# print(my_set)

# Generate Expression
# nums =[1,2,3,4,5,6,7,8,9,10]
# def gen_func(nums):
#         for n in nums:
#             yield n*n
# my_gen = gen_func(nums)

# my_gen  = (n*n for n in nums)

# for i in my_gen:
#     print(i)    


# String Formatting

# person = {'name':'Krishna','age':'3000'}
# sentence = 'The Name of Lord is ' + person['name'] + ' and he is ' + str(person['age'])+ ' years old.'
# print(sentence)

# sentence = 'the name is {} and i am {} years old.'.format(person['name'],person['age'])       
# print(sentence)

# h1 = 'h1'
# text = 'This is Heading'

# sentence  = '<{}>{}</{}>'.format(h1,text,h1)
# print(sentence)

# sentence = 'Name is {0[name]} and age is {0[age]}'.format(person)
# print(sentence)

# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Krishna', '3000')

# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print(sentence)

# sentence = 'Name Is {name} and Age is {age} years old.'.format(name='Krishna',age='3000')
# print(sentence)

# sentence = 'Name Is {name} and Age is {age} years old.'.format(**person)
# print(sentence)

# for i in range(1,11):
#         sentence = 'The Values  is {:02}'.format(i)
#         print(sentence)

# pi = 3.14159265
# sentence = 'The value of Pi is equal To {:.3f}'.format(pi)
# print(sentence)

# sentence = '1 MB is equal to {:,} bytes'.format(1000**2)

# print(sentence)


import datetime

my_date = datetime.datetime(2020, 3, 12, 11, 45, 20)

# print(my_date)

# March 12, 2020

# sentence = '{:%B %d, %Y}'.format(my_date)

# print(sentence)

# March 12, 2020 fell on a Tuesday and was the 061 day of the year.

# sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

# print(sentence)

# os module
# import os
# from datetime import datetime
# print(dir(os))
# print(os.getcwd())
# print(os.listdir())  
# os.mkdir('test-folder')
# os.makedirs('test-folder/second')
# os.removedirs('test-folder')
# os.rename('test-folder', 'Demo-folder')
# print(os.stat('test.py').st_size) # Size of file
# mod_time = os.stat('test.py').st_mtime # Last modified time
# print(datetime.fromtimestamp(mod_time))
# mod_time = os.stat('test.py').st_ctime # Created time
# print(datetime.fromtimestamp(mod_time))

# print(os.environ.get('path'))
# print(os.environ.get('HOME'))

import datetime
# d = datetime.date(2020,3,12)
# tday = datetime.date.today()
tday = datetime.date.today()
# print(tday.year)
# print(tday.month)
# print(tday.day)
# print(tday.weekday()) # Monday is 0 and Sunday is 6
# print(tday.isoweekday()) # Monday is 1 and Sunday is 7
# print(tday.isocalendar()) # (2020, 3, 7)

# tdelta = datetime.timedelta(days=7)
# # print(tday + tdelta)
# # print(tday - tdelta)

# bday = datetime.date(2002,4,5)
# till_bday = tday - bday
# print(till_bday.days)
# print(till_bday.total_seconds())

# t = datetime.time(12,21,45,100000)
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)

# t = datetime.datetime(2002,4,5,12,21,45,100000)
# print(t)
# print(t.year)
# print(t.month)
# print(t.day)
# print(t.hour)

# dt_today = datetime.datetime.today() # Current date and time
# dt_now = datetime.datetime.now() 
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# import pytz
# dt = datetime.datetime(2021,12,28,12,21,45,tzinfo=pytz.UTC)
# print(dt)

# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)


# Sorting list and Tuples

# li = [1,4,6,2,3,6,8,5,7,9,]
# s_li = sorted(li)
# print("Sorted List :\t",s_li)
# li.sort(reverse=True)
# print("Original List :\t",li)

# s_li = sorted(li,reverse=True)
# print("Sorted List In Desending order:\t",s_li)

# tup = (2,4,3,6,7,8,5,9,1)
# s_tup = sorted(tup)
# print("Tuple\t",s_tup)

# dic = { 'name': 'rishu','lang':'python','editor':'vscode'}

# s_dic = sorted(dic)
# print(s_dic)

# li= [10,20,-30,-6,-4,-2,1,3,5,7]
# print(sorted(li,key=abs))


# class Employee():
#         def __init__(self,name,age,salary):
#                 self.name = name
#                 self.age = age
#                 self.salary = salary
                
#         def __repr__(self):
#                 return '({},{},${})'.format(self.name, self.age, self.salary)


# e1 = Employee('Ashiwin',20,1000)
# e2 = Employee('Sorav',23,8000)
# e3 = Employee('Rishabh',20,3000)

# employees = [e1,e2,e3]
# def e_sort(emp):
#         return emp.salary
# s_employees = sorted(employees,key=e_sort)
# # s_employees = sorted(employees,key=e_sort,reverse=True) # For Desending order
# print(s_employees)



# Reading and Writing to Files

# f = open('demo.txt','r')
# print(f.name)
# print(f.mode)
# f.close()
with open('demo.txt','r') as f:
        f_contents = f.read()
        print(f_contents)

