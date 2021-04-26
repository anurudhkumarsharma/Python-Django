my_name = 'rajat'
for i in my_name:
    print(i)

#we can also write
for letters in 'rajat sharma':
     print(letters)

#another one for list
my_list = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in my_list:
    print(a)
    print(b)
    print(c)
    

#this is for dictonaries
d = {'k1':1,'k2':2,'k3':3,'k4':4}
for key,value in d.items():
    print(key)
    print(value)
