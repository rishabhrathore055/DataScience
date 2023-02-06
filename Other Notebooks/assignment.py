import re
f = open("regex_sum_1416444.txt", "r")
sum = 0
for line in f:
    numbers = re.findall('[0-9]+',line) #find all numbers
    for number in numbers:
        sum += int(number)
print(sum)

