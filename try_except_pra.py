
#Problem 2
#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
#
#In [2]:
#x = 5
#y = 0
#z = x/y

try:
    x=5
    y=0
    print(x/y)
except:
    print('enter a valid value of y')
finally:
    print('All Done')