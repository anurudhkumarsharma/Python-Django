#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
# If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

def myfunc(a,b):
    if (a+b==20) or (a==20) or (b==20):
        return True
    else:
        return False