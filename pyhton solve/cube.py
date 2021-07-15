
for i in range(1,7):
      print(i**3,'is the cube of',i)
      i=i+1
else:
    print('done')   



number_of_terms = 5
start = 2
sum = 0
for i in range(0, number_of_terms):
    print(start,end=" ")
    sum += start
    start = (start * 10) + 2
print("\nSum of above series is:", sum)