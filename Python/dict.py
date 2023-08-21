my_dict = {'ridhi':'01','rohit':'02','muskan':'03'}
# print(my_dict)

Emp_details = {'Employee':{'ridhi':{'ID':'01','pay':'2000' ,'Designation':'Data scientist'},
'rohit':{'ID':'02','pay':'3000','designation':'Machine learning engineer'}}}

# print(Emp_details['Employee']['ridhi'])
# Accessing
print(Emp_details.get('ridhi')) 

for x in my_dict.values():
    print(x)

for x,y in my_dict.items():
    print(x,y) 

# Updating
my_dict['muskan'] = '04'
my_dict['tushar'] = '03'

# Deleteing

my_dict.pop('tushar')
print(my_dict)

import pandas as pd

df = pd.DataFrame(Emp_details)
print(df)