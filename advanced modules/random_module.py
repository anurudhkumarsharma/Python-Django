import random
r=random.randint(-100,100)
print(r)

mylist = list(range(0,20))
s=random.choice(mylist)
print(s)

t=(random.sample(population=mylist,k=10))
print(t)

mylist1=[1,2,3,4,5,6,7]
r=random.shuffle(mylist1)
print(mylist1)