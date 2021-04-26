#Write a program to display all prime numbers within a range
# A Prime Number is a whole number that cannot be made by multiplying other whole numbers
#Given:
#start = 25
#end = 50

for i in range(25,51):
    if i%2 == 0 or i%3 == 0 or i%5 == 0:
        print(i,'this is not a prime number')
    else:
        print(i,'this is a prime number')
