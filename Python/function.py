# def add(*t):
#     return sum(t)

# print(add(10,23),end=" ")
# print(add(10,23,43),end=" ")
# print(add(10,30,223,22),end =" ")
# print(add(12,12,32,44,23))


def average(*t):
	A = sum(t)/len(t)
	return A

print(average(10,23),end=" ")
print(average(10,23,43),end=" ")
print(average(10,30,223,22),end =" ")
print(average(12,12,32,44,23))
