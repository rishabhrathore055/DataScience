def fname(*n):
    for i in n:
        print(i,end =" ")

name = ["AA","BB","CC","DD","EE"]
fname(*name)