s={1,2,3}
s.add(4)     #adding an element in a set
print(s)
s.clear()    #slearing an element 
print(s)
s={1,2,3}
sc=s.copy()  #copying a set
print(sc)
s.add(4)
print(s)
print(s.difference(sc))   #check the difference between two sets

#to find the intersection of two sets

s1={1,2,3}
s2={1,5,7}
s1.difference_update(s2)
print(s1)

#to remove a particular element from the set

s={1,2,3}
s.discard(2)
print(s)

#to find the intersection of two sets
s1={1,2,3,4}
s2={1,3,4}
s1.intersection(s2)
print(s2)

#to find the disjoint of settings
s1={1,2,3,4}
s2={1,3,4}
s3={9}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

#to check the subset 
print(s2.issubset(s1))

#to check the superset
print(s1.issuperset(s2))
