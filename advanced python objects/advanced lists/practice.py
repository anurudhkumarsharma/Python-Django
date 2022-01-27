l=[1,2,3]
print(l.count(1))
l.append(4)
print(l)
l.pop(3)
print(l)
l.insert(3,4)
print(l)
l.append([4,5])
print(l)
l.pop()   #pop default value is the last element
print(l)
l.extend([5,6])
print(l)
l.insert(0,'integers')
print(l)
l.reverse()
print(l)
print(l.index(3))

m=[2,4,2,1,7,8,5]
m.sort()
print(m)