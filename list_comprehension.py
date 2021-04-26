# ls =[]
# for i in range(100):
#     if i%3==0:
#         print(i)


#above method can be done in this way:

ls=[i for i in range(100) if i%3==0]
print(ls)


ls=[i**2 for i in range(11)]
print(ls)