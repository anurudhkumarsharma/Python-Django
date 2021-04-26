#Python Program to Print all Prime Numbers in an Interval
#between 900 and 1000



for num in range(900,1001):
    
        for i in range(2,num):
            if (num%i==0):
                print(num,'not a prime number')
                break
        else:
                print(num,'is the prime number')